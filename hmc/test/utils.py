# -*- coding: utf-8 -*-
import uuid
from qiniu import Auth, put_file, etag

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in set(['png', 'jpg', 'jpeg'])

def imageslim(filepath):
    #get ready
    config = {
        "access_key": "2QHQTgGYH8Ow3dy1jpuSKLAlTo-ZkRav1ty2Nok8", 
        "secret_key": "Q91z6hnj5H0LaRkbAN8IPdc8dypdAQ_n21S8tEcu", 
        "bucket_name": "publicbucket", 
        "bucket_domain": "ovorc2c4c.bkt.clouddn.com"
    }
    q = Auth(config['access_key'], config['secret_key'])
    localfile = filepath
    #upload file
    key = str(uuid.uuid1()) + '.png'
    token = q.upload_token(config['bucket_name'], key, 3600)
    ret, info = put_file(token, key, localfile)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
    #get imageslim url
    download_url = 'http://%s/%s' % (config['bucket_domain'], key) + '?imageslim'
    return download_url
