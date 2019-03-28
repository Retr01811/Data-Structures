class tree:
    def __init__(self,ele):
        self.ele=ele
        self.left=None
        self.right=None
def insert(root,ele):
    if root==None:
        root=tree(ele)
    elif root.ele<ele:
        root.right=insert(root.right,ele)
    elif root.ele>ele:
        root.left=insert(root.left,ele)
    return root
def find(root,key):
    if root==None:
        return None
    elif root.ele==key:
        return root
    elif key<root.ele:
        return find(root.left,key)
    elif key>root.ele:
        return find(root.right,key)
def findmin(root):
    if root==None:
        return None
    elif root.left==None:
        return root
    else:
        return findmin(root.left) 
def findmax(root):
    if root==None:
        return None
    elif root.right==None:
        return root.ele
    else:
        return findmax(root.right)
def delete(root,ele):
    if root==None:
        return None
    elif ele<root.ele:
        return delete(root.left,ele)
    elif ele>root.ele:
        return delete(root.right,ele)
    else:
        if root.left==None:
            temp=root.right
            root=None
            return temp
        elif root.right==None:
            temp=root.left
            root=None
            return temp
        else:
            temp=findmin(root.right)
            root.ele=temp.ele
            root.right=delete(root.right,temp.ele)
    return root
def preorder(pos):
    if pos!=None:
        print(pos.ele,end=" ")   
        preorder(pos.left)
        preorder(pos.right)
def odd(pos):
    if pos!=None:
        if (pos.ele)%2!=0:
            print(pos.ele,end=" ")
        odd(pos.left)        
        odd(pos.right)
def swap(root):
    if root:
        swap(root.right)
        swap(root.left)
        (root.left,root.right)=(root.right,root.left)   
                        
c=1
a=tree(int(input("Enter the root element:")))
while c!=0:
    print("\n-------Menu-------")
    print("1.Insert")
    print("2.Find")
    print("3.Find Min")
    print("4.Find Max")
    print("5.Delete")
    print("6.Exit")
    print("7.Odd")
    print("8.Swap")
    n=int(input("Enter the Choice:"))
    if n==1:
        b=int(input('Enter the element:'))
        insert(a,b)
        preorder(a)
    elif n==2:
        b=int(input("Enter the element to be searched:"))
        find(a,b)
    elif n==3:
        findmin(a)
    elif n==4:
        findmax(a)
    elif n==5:
        b=int(input('Enter the element to be deleted:'))
        delete(a,b)
        preorder(a)
    elif n==6:
        c=0
    elif n==7:
        odd(a)
    elif n==8:
        swap(a)    
    else:
        print("Invalid Operation")
        
                






