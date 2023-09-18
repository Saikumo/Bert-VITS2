import subprocess
import time

while True:
    # 执行命令行命令
    command1 = "touch /content/Bert-VITS2/logs/d.pth"
    result = subprocess.run(command1, shell=True)


    command2 = "cp -r /content/Bert-VITS2/logs /content/drive/MyDrive/Bert-VITS2/model"
    result = subprocess.run(command2, shell=True)


    # 等待一个小时
    time.sleep(3600)