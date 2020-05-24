import jetson.inference
import jetson.utils

import argparse
import sys

# parse the command line
parser = argparse.ArgumentParser(description="Classify an image using an image recognition DNN.", 
						   formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.imageNet.Usage())

parser.add_argument("file_in", type=str, help="filename of the input image to process")
parser.add_argument("file_out", type=str, default=None, nargs='?', help="filename of the output image to save")
parser.add_argument("--network", type=str, default="googlenet", help="pre-trained model to load (see below for options)")

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# load an image (into shared CPU/GPU memory)
img, width, height = jetson.utils.loadImageRGBA(opt.file_in)

# load the recognition network
net = jetson.inference.imageNet(opt.network, sys.argv)

for i in range(5):

    # classify the image
    class_idx, confidence = net.Classify(img, width, height)

    # find the object description
    class_desc = net.GetClassDesc(class_idx)

    # print out the result
    print("Trial " + str(i) + ": image is recognized as '{:s}' (class #{:d}) with {:f}% confidence\n".format(class_desc, class_idx, confidence * 100))

    # print out timing info
    net.PrintProfilerTimes()

# overlay the result on the image
if opt.file_out is not None:
    font = jetson.utils.cudaFont(size=jetson.utils.adaptFontSize(width))
    font.OverlayText(img, width, height, "{:f}% {:s}".format(confidence * 100, class_desc), 10, 10, font.White, font.Gray40)
    jetson.utils.cudaDeviceSynchronize()
    jetson.utils.saveImageRGBA(opt.file_out, img, width, height)