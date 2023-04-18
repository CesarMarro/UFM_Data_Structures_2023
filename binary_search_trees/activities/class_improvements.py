'''
Binary Search Tree
'''

class Node:
    """
    Node object
    Args:
        data (str): string value to store in node

    Attributes:
        data (str): value stored in node
        left_child (Node): pointer to node to the left
        right_child (Node): pointer to node to the right
    """
    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None


    def __repr__(self):
        return '({})'.format(self.data)
    

class BinarySearchTree:
    """
    BinarySearchTree object
    Args:
        None

    Attributes:
        root(Node): pointer to first object in tree
    """

    def __init__(self):
        self.root = None

    def delete(self, value: int):
        """
        Delete function
        deletes a node from the binary search tree object 

        Args:
            value (int): value 
        """
        
        if self.root is not None:
            self._delete(value, self.root)
    
    def _delete (self, value: int, subtree: Node):
        print(subtree.data)

        if value < subtree.data:
            subtree.left_child = self._delete(value, subtree.left_child)
        
        if value > subtree.data:
            subtree.right_child = self._delete(value, subtree.right_child)

        if value == subtree.data:
            
            if subtree.left_child is None:
                temp = subtree.right_child
                subtree = None
                return temp
            
            if subtree.right_child is None:
                temp = subtree.left_child
                subtree = None
                return temp
            
            temp = self.find_max(subtree.left_child)
            subtree.data = temp.data
            subtree.left_child = self._delete(self, temp.data, subtree.left_child) 
     
    def insert(self, value: int):
        """Inserts node in the binary search tree class 

        Args:
            value (int): value to add to the tree
        """

        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
        
    def _insert(self, value: int, subtree: Node):

        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')

    
    def traverse(self, subtree: Node):
        """Traverse function

        Args:
            subtree (Node): Node for traverse
        """
        
        print(subtree)
        
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)
    

    def search(self, key: int) -> bool:
        """Search function that searches a key in tree

        Args:
            key (int): value to be searched for

        Returns:
            bool: True if it finds the value on the tree
        """

        if self.root is None:
            return False
        
        else:
            return self._search(key, self.root)


    def _search(self, key: int, subtree: Node) -> bool:

        if key == subtree.data:
            return True
        
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)

        else:
            return False
        

    def find_min(self, subtree: Node) -> int:
        """Function that finds min value

        Args:
            subtree (Node): Subtree where the search begins

        Returns:
            int: returns the Node with the minimun value

        """

        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree


    def find_max(self, subtree: Node) -> int:
        """Function that finds max value

        Args:
            subtree (Node): Subtree where the search begins

        Returns:
            int: returns the Node with the maximun value
            
        """
        while subtree.right_child is not None:
            subtree = subtree.right_child

        return subtree
