import uuid

from main import draw_tree


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

lst = []
def preorder_traversal(root):
    if root:
        lst.append(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)               
        return lst

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


if __name__ == "__main__":
    # Test
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    draw_tree(root)

 
    ### Task_1 ### 
    max = max_value_node(root).val
    print(f'Hайбільше значення в дереві: {max}')

    ### Task_2 ###
    min = min_value_node(root).val
    print(f'Hайменше значення в дереві: {min}')

    ### Task_3 ###
    lst = preorder_traversal(root)
    #print(f"Прямий обхід: {lst}")
    total = 0
    for el in lst:
        total += el
    print(f'Суму всіх значень у дереві: {total}')   