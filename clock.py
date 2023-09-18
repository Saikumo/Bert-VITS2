import subprocess
import time

command1 = "python /content/Bert-VITS2/train_ms.py -m /content/Bert-VITS2/logs/base -c /content/Bert-VITS2/configs/config.json"
result = subprocess.run(command1, shell=True)

while True:
    # 执行命令行命令
    command2 = "cp -r /content/Bert-VITS2/logs /content/drive/MyDrive/Bert-VITS2/model"
    result = subprocess.run(command2, shell=True)


    # 等待一个小时
    time.sleep(60)