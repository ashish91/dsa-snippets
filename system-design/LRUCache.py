class DLLNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.nex = None
        self.prev = None

class DLL:
    def __init__(self, size):
        self.size = size
        self.curr_size = 0
        self.head = None
        self.tail = None

    def print(self):
        if self.head is None:
            return None

        tmp = self.head
        ans = []
        while tmp:
            ans.append("(" + str(tmp.key) + ", " +str(tmp.val) + ")")
            tmp = tmp.nex

        print('->'.join(ans))
        return tmp

    # def find(self, val):
    #     if self.head is None:
    #         return None

    #     tmp = self.head
    #     while tmp and tmp.val != val:
    #         tmp = tmp.nex

    #     return tmp

    # def remove_by_val(self, val):
    #     if self.head is None:
    #         return None

    #     tmp = self.find(val)

    #     if not tmp:
    #         return None

    #     if tmp.prev:
    #         tmp.prev.nex = tmp.nex
    #     if tmp.nex:
    #         tmp.nex.prev = tmp.prev

    #     if tmp.val == self.head.val:
    #         self.head = self.head.nex
    #     elif tmp.val == self.tail.val:
    #         self.tail = self.tail.prev

    #     tmp.nex = tmp.prev = None
    #     self.curr_size -= 1
    #     return tmp

    def remove_node(self, node):
        if self.head is None or node is None:
            return None

        if node == self.head:
            self.head = self.head.nex
        if node == self.tail:
            self.tail = self.tail.prev

        if node.prev:
            node.prev.nex = node.nex
        if node.nex:
            node.nex.prev = node.prev

        node.nex = node.prev = None
        self.curr_size -= 1
        return node

    def remove_from_tail(self):
        if self.tail is None:
            return None

        tmp = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail.prev.nex = None
            self.tail = self.tail.prev

        tmp.prev = None
        self.curr_size -= 1
        return tmp



    def add_to_head(self, node):
        if self.curr_size == self.size:
            self.remove_from_tail

        if self.head is None:
            self.head = self.tail = node
        else:
            node.nex = self.head
            self.head.prev = node
            self.head = node

        self.curr_size += 1
        return node


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.mapping = dict()
        self.dll = DLL(capacity)

    # @return an integer
    def get(self, key):
        if key not in self.mapping:
            return -1

        node = self.mapping[key]
        self.dll.remove_node(node)
        self.dll.add_to_head(node)

        return node.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.mapping:
            node = self.mapping[key]
            node.val = value

            self.dll.remove_node(node)
            self.dll.add_to_head(node)
        else:
            new_node = DLLNode(key,value)

            if self.dll.curr_size == self.capacity:
                removed_node = self.dll.remove_from_tail()
                self.mapping.pop(removed_node.key)
            self.mapping[key] = new_node

            self.dll.add_to_head(new_node)
        return

