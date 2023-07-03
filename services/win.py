import win32serviceutil
import win32service
import win32event
import servicemanager
import sys

import psutil
import subprocess


class SMWinservice(win32serviceutil.ServiceFramework):
    """
       Base class to create winservice in Python
    """

    _svc_name_ = 'pythonService'  # 注册服务名
    _svc_display_name_ = 'Python Service'  # 服务在windows系统中显示的名称
    _svc_description_ = 'Python Service Description'  # 服务描述

    @classmethod
    def parse_command_line(cls):
        """
        ClassMethod to parse the command line
        """
        if len(sys.argv) == 1:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(cls)
            servicemanager.StartServiceCtrlDispatcher()
        else:
            win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        # Create an event which we will use to wait on.
        # The "service stop" request will set this event.
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.stop()
        # Before we do anything, tell the SCM we are starting the stop process.
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # And set my event.
        win32event.SetEvent(self.hWaitStop)
        self.kill_sip_pid()

    def SvcDoRun(self):
        # self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        # win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        self.start()

    def start(self):
        """
        Override to add logic before the start
        eg. running condition
        """
        pass

    def stop(self):
        """
        Override to add logic before the stop
        eg. invalidating running condition
        """
        pass

    @staticmethod
    def kill_sip_pid():
        import time
        time.sleep(1)
        process_name_list = ["pythonservice.exe"]
        for process_name in process_name_list:
            pl = psutil.pids()
            for pid in pl:
                if psutil.Process(pid).name() == process_name:
                    # kill进程
                    find_kill = 'taskkill -f -pid %s' % (pid)
                    subprocess.run(find_kill)
