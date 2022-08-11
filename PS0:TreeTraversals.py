# -------------------------------------------------
# PS0: TreeTraversals
# -------------------------------------------------

# --------------------------------------
# P R O B L E M   S T A T E M E N T 
"""
Given an array of unique elements, construct a Binary Search Tree and print the PreOrder, InOrder and PostOrder Traversals of the tree.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Constraints

1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Output Format

For each test case, print the PreOrder, InOrder and PostOrder Traversals of the Binary Search Tree, separate each traversal by newline. Separate the output of different test cases with an extra newline.

Sample Input 0

3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 
Sample Output 0

1 2 3 4 5 
1 2 3 4 5 
5 4 3 2 1 

3 2 1 4 5 
1 2 3 4 5 
1 2 5 4 3 

4 0 1 5 15 7 17 
0 1 4 5 7 15 17 
1 0 7 17 15 5 4 
"""

# --------------------------------------
# S O L U T I O N   I N   P Y T H O N 

class Node:
    def __init__(self,key):
        self.left= None
        self.right=None
        self.data=key
        
def insert(root, ele): # Function to insert each new node into the binary search tree
    if (root == None):
        return Node(ele)
    if (root.data > ele):
        root.left=insert(root.left,ele)
    else:
        root.right=insert(root.right,ele)
    return root
  
def preorder(root):
    if(root==None):
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
    
    
def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
    
def postorder(root):
    if(root==None):
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
    
# Trunc Code
tc=int(input())
for _ in range(tc):
    n=int(input())
    
    val=[int(num) for num in input().split()]
    
    root=None
    
    for d in range(len(val)):
        root= insert(root,val[d])
    # BST created
    
    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)
    print()
    
    print()

# -----------------------------------------


