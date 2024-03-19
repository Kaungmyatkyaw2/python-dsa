class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, child):
        self.children.append(child)
