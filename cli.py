
# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/3 16:57
@Auth ： 七月
@File ：cli.py
@IDE ：PyCharm
"""
import os

from flask import Flask,render_template,request,send_file
from makeLog import Logger
from xmindPars import dataParWriteExcel

app = Flask(__name__,static_url_path='/static')
log = Logger()


def exisDir(file_name):
    xmind_dir = os.path.join(os.getcwd(), 'upload')
    excel_dir = os.path.join(os.getcwd(), 'download')


    if file_name.split('.')[1] == 'xmind':
        if not os.path.exists(xmind_dir):
            os.mkdir(xmind_dir,0o777)
            log.info('目录不存在正在创建:'+xmind_dir)
            return xmind_dir
        log.info(xmind_dir+'目录已存在，不再创建')
        return xmind_dir
    else:
        if not os.path.exists(excel_dir):
            os.mkdir(excel_dir,0o777)
            log.info('目录不存在正在创建:' + excel_dir)
            return excel_dir
        log.info(excel_dir + '目录已存在，不再创建')
        return excel_dir

def delFile(file_name):
    '''
    判断上传前是否有重复文件，如果有就先删除再上传
    :param file_name:
    :return:
    '''
    dir = exisDir(file_name)
    path = os.path.join(dir,file_name)
    if os.path.exists(path):
        os.remove(path)
        log.info('已存在相同的文件准备删除旧的文件:'+path)
        return True
    else:
        return False


@app.route('/x2e')
def index():
    return render_template('index.html')



@app.route('/x2e/upload', methods=['POST'])
def uploadFileHhandler():
    #获取前端上传的文件
    file = request.files['file']
    #上传前先检查目录是否存在，不存在则创建
    xmind_dir = exisDir(file.filename)
    #上传前先删除目录下同名文件
    delFile(file.filename)
    #保存文件至目录
    xmind_path = os.path.join(xmind_dir,file.filename)
    file.save(xmind_path)
    log.info('上传文件成功：'+file.filename)

    #开始解析文件

    excel_file_name = xmind_path.split(xmind_dir)[1].split(".")[0][1:] + "测试用例.xlsx"

    excel_dir = exisDir(excel_file_name)

    excel_path = os.path.join(excel_dir,excel_file_name)

    dataParWriteExcel(xmind_path,excel_path)
    log.info('解析xmind成功，生成excel成功')
    app.config['excel_path'] = excel_path
    return excel_path


@app.route('/x2e/download')
def downLoadFile():

    if os.path.exists(app.config['excel_path']):
        log.info('下载文件成功:'+app.config['excel_path'])
        return send_file(app.config['excel_path'],as_attachment=True)
    else:
        return app.config['excel_path']+'文件不存在'

