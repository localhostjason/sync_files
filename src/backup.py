# -*- coding:utf8 -*-
from config import Config

"""
paramiko 从远处服务器下载文件资源到本地
Date: 2021-08-27
"""

import paramiko
import os
from stat import S_ISDIR


def down_from_remote(sftp, remote_dir_name, local_dir_name):
    """远程下载文件"""
    remote_file = sftp.stat(remote_dir_name)
    if S_ISDIR(remote_file.st_mode):
        # 文件夹，不能直接下载，需要继续循环
        check_local_dir(local_dir_name)
        print('开始下载文件夹：' + remote_dir_name)
        for remote_file_name in sftp.listdir(remote_dir_name):
            sub_remote = os.path.join(remote_dir_name, remote_file_name)
            sub_remote = sub_remote.replace('\\', '/')
            sub_local = os.path.join(local_dir_name, remote_file_name)
            sub_local = sub_local.replace('\\', '/')
            down_from_remote(sftp, sub_remote, sub_local)
    else:
        # 文件，直接下载
        print('开始下载文件：' + remote_dir_name)
        sftp.get(remote_dir_name, local_dir_name)


def check_local_dir(local_dir_name):
    """本地文件夹是否存在，不存在则创建"""
    if not os.path.exists(local_dir_name):
        os.makedirs(local_dir_name)


def backup_file():
    t = paramiko.Transport(Config.host_name, Config.port)
    t.connect(username=Config.user_name, password=Config.password)

    sftp = paramiko.SFTPClient.from_transport(t)

    # 远程文件开始下载
    down_from_remote(sftp, Config.remote_dir, Config.local_dir)
