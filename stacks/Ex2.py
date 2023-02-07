from stack import Stack 
arr = [1,2,3,4,5]
arr2 = []

stack = Stack(len(arr))

for i in range (len(arr)):
    stack.push(arr[i])

print(stack)


while (stack.top != -1):
    arr2.append(stack.pop())

print(arr2)