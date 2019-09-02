class Node(object):
    def __init__(self, item):
        self.next = None
        self.item = item


class SimpleLinkList(object):
    def __init__(self):
        self._head = None

    # search(item) 查找节点是否存在
    def search(self, item):
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    # remove(item) 删除节点
    def remove(self, item):
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:
                    self._head = self._head.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    # length() 链表长度
    def length(self):
        count = 0
        cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next

        return count

    # is_empty() 链表是否为空
    def is_empty(self):
        return self._head == None

    # add(item) 链表头部添加元素
    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    # insert(pos, item) 指定位置添加元素
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            node = Node(item)
            count = 0
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    # append(item) 链表尾部添加元素
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    # travel() 遍历整个链表
    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.item, end='->')
            cur = cur.next
        print('')


s = SimpleLinkList()
# s.add(1)
# s.add(2)
s.append(3)
print(s.length())
s.insert(1, 2)
s.insert(-1, 4)
s.travel()
s.remove(4)
s.travel()
print(s.search(1))
print(s.is_empty())
