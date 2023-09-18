import subprocess
import time

while True:
    # 执行命令行命令
    command = "ls"
    result = subprocess.run(command, shell=True)

    # 打印命令执行结果
    print("命令执行结果:")
    print(result)

    # 等待一个小时
    time.sleep(3600)