## SYNC FILES

在windows中注册服务，每小时定时轮询，从服务器端（Linux）下载文件 到本地目录（windows）。具体配置见 config.py:

```python
# 远程服务器连接信息
host_name = '192.168.0.103'
user_name = 'root'
password = '1'
port = 22
# 远程文件路径（需要绝对路径）
remote_dir = '/usr/local/src/test'

# 本地文件存放路径 
local_dir = os.path.join(BASE_DIR, 'backup')
```



### 运行环境

- python3+
- winodws



#### 技术

- pywin32  “Windows serivice 服务”
- apscheduler  “定时 轮询”
- paramiko "远程下载文件"



### 运行前配置环境变量

```
C:\Python\Python37\lib\site-packages\win32;
C:\Python\Python37\lib\site-packages\pywin32_system32;
C:\Python\Python37\Scripts\;
C:\Python\Python37\;
```



### 安装步骤

```
注册服务 python main.py install
注册服务并且使开机自启动 python main.py --startup auto install
更新服务 python main.py update
卸载服务 python main.py remove
查看服务 mmc Services.msc 或者 打开任务管理器查看
启动服务 net start <service name> 或者 python xxx.py start
停止服务 net stop <service name> 或者 python xxx.py stop
重启服务 net restart <service name> 或者 python xxx.py restart
```



### 注意

1. 关闭杀毒软件
