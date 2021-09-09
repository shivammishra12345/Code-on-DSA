class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DL:
    def __init__(self):
        self.head=None
    def ad(self,data):
        newnode=node(data)
        current=self.head
        if(self.head):
            while(current.next):
                current=current.next
            t=current.next
            current.next=newnode
            t.prev=current
            t.next=None
                
            
        else:
            self.head=newnode
            
            
    def insert(self,data1,n):
        newnode=node(data1)
        m=int(input("enter the position"))
        if(self.head==None):
            print("it is an empty dl ")
        elif(m==1):
            p=self.head
            t=p.next
            p.next=newnode
            t.next=p
            t.prev=None
        else:
            i=1
            p=self.head
            while(i<=m-1):
                p=p.next
                i=i+1
            t=p.next
            p.next=newnode
            t.prev=newnode
            newnode.prev=p
    def pLL(self):
        current=self.head
        while(current.next):
            print(current.data)
            current=current.next
x=DL()
x.ad(1)
x.ad(2)
x.pLL()
x.insert(3,1)
x.pLL()
        
            
            
                
                
                
            
        
