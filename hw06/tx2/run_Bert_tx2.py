import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data
import sys, os
import numpy as np
import pandas as pd
from tqdm import tqdm, tqdm_notebook
from pytorch_pretrained_bert import convert_tf_checkpoint_to_pytorch
from pytorch_pretrained_bert import BertTokenizer, BertForSequenceClassification,BertAdam
from pytorch_pretrained_bert.modeling import BertModel
from pytorch_pretrained_bert import BertConfig

MAX_SEQUENCE_LENGTH = 220

def convert_lines(example, max_seq_length,tokenizer):
    max_seq_length -=2
    all_tokens = []
    longer = 0
    for text in tqdm(example):
        tokens_a = tokenizer.tokenize(text)
        if len(tokens_a)>max_seq_length:
            tokens_a = tokens_a[:max_seq_length]
            longer += 1
        one_token = tokenizer.convert_tokens_to_ids(["[CLS]"]+tokens_a+["[SEP]"])+[0] * (max_seq_length - len(tokens_a))
        all_tokens.append(one_token)
    return np.array(all_tokens)

# config
device = torch.device("cuda")

BERT_MODEL_PATH = 'data/uncased_L-12_H-768_A-12'
bert_config = BertConfig('bert_config.json')
model_file = 'bert_pytorch.bin'
batch_size = 1

# preprocessing
tokenizer = BertTokenizer.from_pretrained(BERT_MODEL_PATH, cache_dir=None,do_lower_case=True)
test_all = pd.read_csv("data/test.csv")
test_all = test_all.iloc[:10,:]
test_all['comment_text'] = test_all['comment_text'].astype(str)
test_X = convert_lines(test_all["comment_text"].fillna("DUMMY_VALUE"),MAX_SEQUENCE_LENGTH,tokenizer)
test_all=test_all.fillna(0)

# load model and perform inference
model = BertForSequenceClassification(bert_config,num_labels=1)
model.load_state_dict(torch.load(model_file))
model.to(device)

for param in model.parameters():
    param.requires_grad=False
model.eval()

test_preds = np.zeros((len(test_X)))
test = torch.utils.data.TensorDataset(torch.tensor(test_X, dtype=torch.long))
test_loader = torch.utils.data.DataLoader(test, batch_size=batch_size, shuffle=False)

tk0 = tqdm(test_loader)
for i,(x_batch,)  in enumerate(tk0):
    pred = model(x_batch.to(device), attention_mask=(x_batch>0).to(device), labels=None)
    test_preds[i*batch_size:(i+1)*batch_size]=pred[:,0].detach().cpu().squeeze().numpy()

preds = torch.sigmoid(torch.tensor(test_preds))
for i in range(len(test_all)):
    print(test_all["comment_text"][i], preds[i])
    print("---" * 20)

