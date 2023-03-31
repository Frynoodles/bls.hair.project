import os
import datetime


# 暂时只有记录正常信息和错误信息的需求

LOG_PATH: str = "./log/"

def now_time()->str:
    """获取格式化的当前时间

    Returns:
        str: 当前时间
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Logger:
    def __init__(self, name: str) -> None:
        """初始化

        Args:
            name (str): 需要日志的程序名，一般为文件名
        """
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
        self.log_path: str = f"{LOG_PATH}log_{name}.txt"
        self.error_path: str = f"{LOG_PATH}error_{name}.txt"
        if not os.path.exists(self.log_path):
            file = open(self.log_path, "x")
            file.close()
        if not os.path.exists(self.error_path):
            file = open(self.error_path, "x")
            file.close()

    def log(self, msg: str):
        """记录正常信息

        Args:
            msg (str): 信息内容
        """
        file=open(self.log_path,'a',encoding='utf-8')
        file.write(f'{now_time()}\t{msg.strip()}\n')
        file.close()

    def error(self, msg: str):
        """记录错误

        Args:
            msg (str): 错误信息
        """
        file=open(self.error_path,'a',encoding='utf-8')
        file.write(f'{now_time()}\t{msg.strip()}\n')
        file.close()


if __name__=='__main__':
    # print(now_time())
    pass