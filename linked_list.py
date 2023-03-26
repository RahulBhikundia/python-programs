#Program for Singly Linked List

class node:
    def __init__(self,data = 0):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    
    def insert_front(self,data) -> None:
        new = node(data)
        if self.head == None:
            self.head = new
            return
        new.next = self.head
        self.head = new
        return

    def insert_end(self,data) -> None:
        new = node(data)
        if self.head == None:
            self.head = new
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new
        return

    def del_front(self) -> None:
        if self.head == None:
            print("UnderFlow!!")
            return
        print("Removed Data:",self.head.data)
        self.head = self.head.next
        return

    def del_end(self) -> None:
        if self.head == None:
            print("UnderFlow!!")
            return
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        print("Removed Data:",temp.next.data)
        temp.next = None
        return

    def printLL(self) -> None:
        temp = node()
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
        
# Definition of class ends here

if __name__ == "__main__":
    ll = LL()
    ll.insert_front(1)
    ll.insert_front(2)
    ll.insert_front(3)
    ll.insert_front(4)
    ll.insert_front(5)
    ll.printLL()
    ll.del_front()
    ll.del_end()
    ll.printLL()