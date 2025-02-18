class myStack:
     def __init__(self):
          self.stack = list()

     def isEmpty(self):
          if len(self.stack) == 0:
               return True
          else:
               return False

     def push(self, item):
          self.stack.append(item)

     def pop(self):
          if len(self.stack) != 0:
               return self.stack.pop()

     def peek(self):
          if len(self.stack) != 0:
               return self.stack[-1]
          else:
               return -1

     def size(self):
          return len(self.stack)

     def show(self):
          for element in self.stack:
               print(element)


s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())

