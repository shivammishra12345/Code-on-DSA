class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LL:
    
    def __init__(self):
        self.head=None
        
    def ad(self,data):
        newnode=node(data)
        if (self.head!=None):
            current=self.head
            while(current.next):
                current=current.next
            current.next=newnode
        else:
            self.head=newnode
    def pLL(self):
        if (self.head==None):
            print("list is empty")
        else:
            current=self.head
            while(current):
                print(current.data)
                current=current.next
    def insert(self,data1,n):
        newnode=node(data1)
        if(self.head==None):
            self.head=newnode
        else:
            current=self.head
            while(current.data!=n):
                current=current.next
            p=current.next
            current.next=newnode
            newnode.next=p
    def delete(self,n):
        if(self.head==None):
            print("list is not form till now")
        elif(n==-1):
            temp=self.head
            self.head=temp.next
            del(temp)
            
        else:
            current=self.head
            while(current.data!=n):
                current=current.next
            p=current.next
            current.next=p.next
            del(p)


            
x=LL()

while(True):
    
    b=int(input("enter the choice which opertaion would you like to perform\n press1 to add node in Llist \n pess2 to insert node in Llist \n press3 to delete element \n press4 to exit="))
    if(b==1):
        c=int(input("enter the data"))
        
        x.ad(c)
        x.pLL()
    elif(b==2):
        c=int(input("enter the data"))
        d=int(input("enter the number after which you want to enter the data"))
        x.insert(c,d)
        x.pLL()
    elif(b==3):
        d=int(input("enter the number which is present before the number which you want to delete"))
        if(d in x):
            if(d==x.head.data):
                x.delete(-1)
                x.pLL()
            else:
                x.delete(d)
                x.pLL()
        else:
            print("number not present in list")
    else:
        x.pLL()
        break

        


            
            
        
            
            
