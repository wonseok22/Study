N = int(input())
tree = dict()
for _ in range(N):
    parent,left,right = input().split()
    tree[parent] = {
        "left" : left,
        "right" : right
    }
def preorder(curr):
    if curr != ".":
        print(curr,end="")
        preorder(tree[curr]["left"])
        preorder(tree[curr]["right"])

def inorder(curr):
    if curr != ".":
        inorder(tree[curr]["left"])
        print(curr,end="")
        inorder(tree[curr]["right"])

def postorder(curr):
    if curr != ".":
        postorder(tree[curr]["left"])
        postorder(tree[curr]["right"])
        print(curr,end="")

preorder("A")
print("")
inorder("A")
print("")
postorder("A")