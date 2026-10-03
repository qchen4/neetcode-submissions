class Deque:
    
    def __init__(self):
        self.data = []


    def isEmpty(self) -> bool:
        return not self.data

    def append(self, value: int) -> None:
        if not self.isEmpty():
            self.data.append(value)
        else:
            self.data = [value]

    def appendleft(self, value: int) -> None:
        self.data = [value] + self.data

    def pop(self) -> int:
        if not self.isEmpty():
            item = self.data[-1]
            self.data = self.data[:len(self.data)-1]
            return item
        return -1

    def popleft(self) -> int:
        if not self.isEmpty():
            item = self.data[0]
            self.data = self.data[1::]
            return item
        return -1
        
