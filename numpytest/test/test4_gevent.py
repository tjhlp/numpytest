import time
from gevent import monkey
import gevent
monkey.patch_all()


def work1():
    for i in range(5):
        print("work1 -----1")
        time.sleep(0.5)


def work2():
    for i in range(5):
        print("work2 -----2")
        time.sleep(0.5)


# 创建携程并指派任务
g1 = gevent.spawn(work1)
g2 = gevent.spawn(work2)

# 等待协程执行完成再关闭主线程
g1.join()
g2.join()




