from TreeNode import TreeNode

def preOrder(root):
    if len(root.children) == 0:
        print(root.value)
    else:
        print(root.value)
        for i in range(len(root.children)):
            preOrder(root.children[i])



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

    preOrder(root)


main()
