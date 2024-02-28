from main.ds.stack.Stack import Stack

greet = "Hello"

stack = Stack(20)

for i in range(len(greet)):
    stack.push(greet[i])

reverse = ""
while not stack.isEmpty():
    reverse = reverse + stack.pop()

print("Reveresed Word : ", reverse)
