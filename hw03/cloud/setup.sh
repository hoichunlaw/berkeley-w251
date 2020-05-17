mkdir -m 777 /mnt/face_images_gray
s3fs cloud-object-storage-v7-cos-standard-c5s /mnt/face_images_gray -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.jp-tok.cloud-object-storage.appdomain.cloud
mkdir -m 777 /mnt/face_images_gray/hw03
