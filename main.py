import datetime
import logging
import os
import sys

from apscheduler.schedulers.blocking import BlockingScheduler

from config import Config
from services.win import SMWinservice
from src.backup import backup_file

logging.basicConfig(
    filename=os.path.join(Config.LOG_DIR, 'data-sync-service.log'),
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-7.7s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p'
)


class BackupFileService(SMWinservice):
    _svc_name_ = "SyncRemoteFile"  # 注册服务名
    _svc_display_name_ = "Sync remote file"  # 服务在windows系统中显示的名称
    _svc_description_ = "Sync remote file to local dir"  # 服务描述

    @staticmethod
    def schedule():
        scheduler = BlockingScheduler()

        # 定时 每小时执行一次
        scheduler.add_job(backup_file,
                          'interval',
                          hours=1,
                          # seconds=3,
                          id='backup_file',
                          misfire_grace_time=600,
                          next_run_time=datetime.datetime.now(),
                          coalesce=True,
                          replace_existing=True)

        logging.info("sync job start.")
        return scheduler

    def start(self):
        logging.info(f"data sync start monitor.")
        self.schedule().start()

    def stop(self):
        logging.info(f"data sync stop monitor.")
        try:
            self.schedule().shutdown()
        except Exception as e:
            logging.debug(e)


if __name__ == '__main__':
    # 注册服务
    BackupFileService.parse_command_line()
    # backup_file()
    pass
