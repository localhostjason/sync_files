import os


class Config:
    NAME = "SYNC FILE"
    TIME = "2021-08-27"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    LOG_DIR = os.path.join(BASE_DIR, 'log')

    # 远程服务器连接信息
    host_name = '192.168.120.249'
    user_name = 'root'
    password = '1'
    port = 22
    # 远程文件路径（需要绝对路径）
    remote_dir = '/home/backup'

    # 本地文件存放路径
    local_dir = os.path.join(BASE_DIR, 'backup')
