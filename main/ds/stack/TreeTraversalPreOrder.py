# Making Preorder without using lang's method stack (use our own stack)

#  TreeTraversel.py in recursion folder there is some importing Stack err in that file so I implemented
# Traversel algo using stack in this file ( I don't know how to solve that import err cause I am lack of python knowledge and I also don't wanna spend many time on python err)

from TreeNode import TreeNode
from Stack import Stack


def preOrderIterative(root):
    stack = Stack(20)
    stack.push(root)

    while not stack.isEmpty():
        node = stack.pop()
        print(node.value)

        childLen = len(node.children)

        if childLen > 0 :
            i = childLen - 1
            while i >= 0:
                stack.push(node.children[i])
                i-=1


def main():
    root = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")
    g = TreeNode("G")

    root.addChild(b)
    b.addChild(c)
    b.addChild(d)
    root.addChild(e)
    e.addChild(f)
    e.addChild(g)

    preOrderIterative(root)


main()
