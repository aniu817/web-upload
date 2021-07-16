#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/14 14:30
# @Author : liu yang
# @Desc: 文件上传后端接口


# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from common.path_helper import PathHelper
import pypinyin

app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        # print(request.files['file'])
        load_path = PathHelper().get_package_dir('file')
        # file_name = secure_filename(''.join(pypinyin.lazy_pinyin(file.filename)))
        file_name = file.filename
        file.save(load_path + '/' + file_name)
        # return 'file uploaded successfully'
        return '上传成功'


if __name__ == '__main__':
    app.run()
