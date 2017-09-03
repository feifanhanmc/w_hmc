# -*- coding: utf-8 -*-
import os
import shutil
from flask import Blueprint, render_template, abort, request
from werkzeug import secure_filename
from hmc.test.utils import imageslim, allowed_file

test_bp = Blueprint('test', __name__)

@test_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    file_dir=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'upload')
    if os.path.exists(file_dir):
        shutil.rmtree(file_dir)  
    os.makedirs(file_dir)
    
    if request.method == 'POST':
        file = request.files['upload_file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(file_dir, filename)
            file.save(filepath)
            download_url = imageslim(filepath)
            return download_url
        return 'Error'
    return render_template('test/upload.html')   




