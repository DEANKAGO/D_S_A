class stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    #push
    def push(self, value):
        self.list.append(value)
        return "Element have been successfully inserted"
    
    #pop
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        
    #peek
    def peek(self):
        if self.isEmpty():
            return "The is no element in the stack"
        else:
            return self.list[len(self.list)-1]
        
    #delete
    def delete(self):
        self.list = None
    