import os
# 调用shell 脚本
val = os.system('ls -al')
print(f"返回值 -> {val}")
