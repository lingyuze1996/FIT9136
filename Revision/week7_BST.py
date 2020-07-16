class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def traversal(self):
        tr(self.root)

    def append(self, item):
        if self.root is None:
            self.root = Node(item)
            return

        current = self.root
        while True:
            if item < current.item:
                if current.left is None:
                    current.left = Node(item)
                    break
                else:
                    current = current.left

            if item > current.item:
                if current.right is None:
                    current.right = Node(item)
                    break
                else:
                    current = current.right


def tr(node):
    current = node
    if current.left is None and current.right is None:
        print(current.item, " ")
    elif current.left is not None:
        tr(node.left)
        if current.right is not None:
            tr(node.right)


def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = int(n / 2)

    l = merge_sort(alist[:mid])
    r = merge_sort(alist[mid:])

    l_i = 0
    r_i = 0
    result = []

    while l_i < len(l) and r_i < len(r):
        if l[l_i] <= r[r_i]:
            result.append(l[l_i])
            l_i += 1
        else:
            result.append(r[r_i])
            r_i += 1
    result += l[l_i:]
    result += r[r_i:]
    return result


def search_1(my_list, search_value):
    first = 0
    last = len(my_list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if my_list[mid] == search_value:
            found = True
        else:
            if search_value < my_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

search_1([1, 2, 3, 5, 6, 8, 9],3)

