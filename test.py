import threading
import time

print('test')
print("test test")

def sing():
    while True:
        print("sing。。。")
        time.sleep(1)

def dance():
     while True:
        print("dance...")
        time.sleep(1)

if __name__ == "__main__":
#多线程
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)

    thread_sing.start()
    thread_dance.start()
