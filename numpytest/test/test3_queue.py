import multiprocessing

queue = multiprocessing.Queue()
queue.put('1')
queue.put('2')
queue.put('3')

print("取值前消息数量：", queue.qsize())
print(queue.get())
print("取值前消息数量：", queue.qsize())
print(queue.get())
print("取值前消息是否为空：", queue.empty())
print(queue.get())
print("取值前消息是否为空：", queue.empty())



