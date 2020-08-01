# @brief This class holds the fields required for a single node in AVL
class AvlNode:
    # @brief This function initializes the class object
    # @param[in] key Key of the node
    # @param[in] value Value of the node
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

# @brief This class manages provides an Dictionary ADT using AVL Trees
class AvlTree:
    # @brief This function initializes the class object
    def __init__(self):
        self.__root = None

    # @brief Given a node object this function returns the height of that node
    # @param[in] node Node whose height is to be returned
    # @retval Integer height (0 for None)
    def get_height(self, node):
        # Height is zero for None
        if not node:
            return 0
        else:
             return node.height

    # @brief This function calculates the height of the current node using
    #        heights of the left and the right subtrees
    # @param[in] node Node whose height is to be returned
    # @retval Integer height (0 for None)
    def calculate_height(self, node):
        # Height is zero for None
        if not node:
            return 0
        # Height of the root is one plus the maximum of height of left and right
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    # @brief This function performs a single right rotation on a pair of nodes
    # @param[in] node1 The node which suffered from imbalance
    # @param[in] node2 The node which is to the left of node1
    # @retval node2 The new subtree formed after rotation
    def __rotate_right(self, node1, node2):
        # Adjust the pointers
        node1.left = node2.right
        node2.right = node1

        # Adjust the height of the rotated nodes
        node1.height = self.calculate_height(node1)
        node2.height = self.calculate_height(node2)

        return node2

    # @brief This function performs a single left rotation on a pair of nodes
    # @param[in] node1 The node which suffered from imbalance
    # @param[in] node2 The node which is to the right of node1
    # @retval node2 The new subtree formed after rotation
    def __rotate_left(self, node1, node2):
        # Adjust the pointers
        node1.right = node2.left
        node2.left = node1

        # Adjust the height of the rotated nodes
        node1.height = self.calculate_height(node1)
        node2.height = self.calculate_height(node2)

        return node2

    # @brief This function balances a node and performs rotations if necessary
    # @param[in] node Node object or pointer to be balanced
    # @retval Returns balanced node object or pointer
    def __balance_node(self, node):
        # Calculate the balance factor of the current node
        balance_factor = self.get_height(node.left) - self.get_height(node.right)

        # If left heavy
        if balance_factor > 1:
            # Find the balance factor of the node to the left
            balance_factor = self.get_height(node.left.left) - self.get_height(node.left.right)
            # Extra rotation for LR imbalance
            if balance_factor < 0:
                node.left = self.__rotate_left(node.left, node.left.right)
            # Mandatory rotation for LR and LL imbalance
            node = self.__rotate_right(node, node.left)

        # If right heavy
        elif balance_factor < -1:
            # Find the balance factor of the node to the right
            balance_factor = self.get_height(node.right.left) - self.get_height(node.right.right)
            # Extra rotation for RL imbalance
            if balance_factor > 0:
                node.right = self.__rotate_right(node.right, node.right.left)
            # Mandatory rotation for RL and RR imbalance
            node = self.__rotate_left(node, node.right)

        # If balanced
        else:
            node.height = self.calculate_height(node)

        return node

    # @brief This function recursively inserts a key value pair in the tree
    # @param[in] root Node pointer or object
    # @param[in] key Key to be inserted
    # @param[in] value Value to be inserted
    # @retval Node pointer or object
    def __insert_recursive(self, root, key, value):
        # Check if root is null
        if not root:
            return AvlNode(key, value)
        # If key is less than current key
        elif key < root.key:
            root.left = self.__insert_recursive(root.left, key, value)
        # If key is greater than current key
        else:
            root.right = self.__insert_recursive(root.right, key, value)

        # Balance and return the node
        return self.__balance_node(root)

    # @brief The function available for the user to insert a key value pair
    # @param[in] key Key to be inserted
    # @param[in] value Value to be inserted
    def insert(self, key, value):
        self.__root = self.__insert_recursive(self.__root, key, value)

    # @brief The function recursively finds for a key and updates
    #        its values field by the specified value
    # @param[in] root Node pointer or object
    # @param[in] key Key to be searched for
    # @param[in] value Value to be updated with
    # @retval True If key found and updated
    # @retval False If key not found
    def __update_recursive(self, root, key, value):
        # If root is None then return false
        if not root:
            return False
        # If key is less than current key
        elif key < root.key:
            return self.__update_recursive(root.left, key, value)
        # If key is greater than current key
        elif key > root.key:
            return self.__update_recursive(root.right, key, value)
        # If key found
        else:
            # Update the current node
            root.value = value
            # Return true
            return True

    # @brief The function available for the user to update a key's value
    # @param[in] key Key to be searched for
    # @param[in] value Value to be updated with
    def update(self, key, value):
        return self.__update_recursive(self.__root, key, value)

    # @brief This function deleted a node recursively from the tree
    # @param[in] root Node object or pointer to be deleted
    # @param[in] key Key to be deleted
    # @retval Node pointer or object
    def __delete_recursive(self, root, key):
        # If root is None then return false
        if not root:
            return None
        # If key is less than current key
        elif key < root.key:
            root.left = self.__delete_recursive(root.left, key)
        # If key is greater than current key
        elif key > root.key:
            root.right = self.__delete_recursive(root.right, key)
        # If key found
        else:
            # If root has not child
            if not root.left and not root.right:
                del root
                return None
            # If root has only left child
            elif root.left and not root.right:
                ret_node = root.left
                del root
                return ret_node
            # If root has only right child
            elif root.right and not root.left:
                ret_node = root.right
                del root
                return ret_node
            # If root has both childs
            else:
                # Get the next successor for the current node
                successor = root.right
                while successor.left:
                    successor = successor.left

                # Move the successor to the current node
                root.key = successor.key
                root.value = successor.value

                # Delete the successor node
                root.right = self.__delete_recursive(root.right, successor.key)

        return self.__balance_node(root)

    # @brief The function available to the user to delete a node from the tree
    # @param[in] key Key to be deleted from the tree
    def delete(self, key):
        self.__root = self.__delete_recursive(self.__root, key)

    # @brief This function performs an ascending traversal of the tree
    #        printing the key value pair while traversing
    # @param[in] root Node object or pointer
    def __print_asc_recursive(self, root):
        if not root:
            return

        # Go left
        self.__print_asc_recursive(root.left)

        # Write the current key and values to the file
        print(root.key, ":", root.value)

        # Go right
        self.__print_asc_recursive(root.right)

    # @brief The function available for the user to print the tree in
    #        ascending order
    def print_asc(self):
        self.__print_asc_recursive(self.__root)

    # @brief This function performs an desceding traversal of the tree
    #        printing the key value pair while traversing
    # @param[in] root Node object or pointer
    def __print_desc_recursive(self, root):
        if not root:
            return

        # Go right
        self.__print_desc_recursive(root.right)

        # Write the current key and values to the file
        print(root.key, ":", root.value)

        # Go left
        self.__print_desc_recursive(root.left)

    # @brief The function available for the user to print the tree in
    #        descending order
    def print_desc(self):
        self.__print_desc_recursive(self.__root)

    # @brief This function recursively searches for a key in a tree
    # @param[in] root Node object or pointer
    # @param[in] key Key to be searched formed
    # @retval Returns the value corresponding to the key or None
    def __search_recursive(self, root, key):
        # If root is None then return false
        if not root:
            return None
        # If key is less than current key
        elif key < root.key:
            return self.__search_recursive(root.left, key)
        # If key is greater than current key
        elif key > root.key:
            return self.__search_recursive(root.right, key)
        # If key found
        else:
            return root.value

    # @brief The function available to the user to search for key's value
    # @param[in] key Key to be searched formed
    def search(self, key):
        return self.__search_recursive(self.__root, key)
