# @brief This class holds the fields required for a single node in AVL
class AvlNode:
    # @brief This function initializes the class object
    # @param[in] key Key of the node
    # @param[in] value Value of the node
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
        self.height = 1
        self.left = None
        self.right = None

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

        # Calculate the balance factor of the current node
        balance_factor = self.get_height(root.left) - self.get_height(root.right)

        # If left heavy
        if balance_factor > 1:
            # Extra rotation for LR imbalance
            if key > root.left.key:
                root.left = self.__rotate_left(root.left, root.left.right)
            # Mandatory rotation for LR and LL imbalance
            root = self.__rotate_right(root, root.left)

        # If right heavy
        elif balance_factor < -1:
            # Extra rotation for RL imbalance
            if key < root.right.key:
                root.right = self.__rotate_right(root.right, root.right.left)
            # Mandatory rotation for RL and RR imbalance
            root = self.__rotate_left(root, root.right)

        # If balanced
        else:
            root.height = self.calculate_height(root)

        return root

    # @brief The function available for the user to insert a key value pair
    # @param[in] key Key to be inserted
    # @param[in] value Value to be inserted
    def insert(self, key, value):
        self.__root = self.__insert_recursive(self.__root, key, value)

    # @brief The function recursively finds for a key and updates
    #        its values field by appending the specified value to its list
    # @param[in] root Node pointer or object
    # @param[in] key Key to be searched for
    # @param[in] value Value to be appended
    # @retval True If key found and updated
    # @retval False If key not found
    def __find_and_update_recursive(self, root, key, value):
        # If root is None then return false
        if not root:
            return False
        # If key is less than current key
        elif key < root.key:
            return self.__find_and_update_recursive(root.left, key, value)
        # If key is greater than current key
        elif key > root.key:
            return self.__find_and_update_recursive(root.right, key, value)
        # If key found
        else:
            # Update the current node
            root.value.append(value)
            # Return true
            return True

    # @brief The function available for the user to update a key's value
    # @param[in] key Key to be searched for
    # @param[in] value Value to be appended
    def find_and_update(self, key, value):
        return self.__find_and_update_recursive(self.__root, key, value)

    # @brief This function performs an inorder traversal of the tree
    #        printing the key value pair while traversing
    # @param[in] root Node object or pointer
    # @param[in] fp File pointer to the result file
    def __inorder_recursive(self, root, fp):
        if not root:
            return

        # Go left
        self.__inorder_recursive(root.left, fp)

        # Write the current key and values to the file
        fp.write("{}: ".format(root.key))
        for line_no in root.value:
            fp.write("{} ".format(line_no))
        fp.write("\n")

        # Go right
        self.__inorder_recursive(root.right, fp)

    # @brief The function available for the user to print the tree in
    #        ascending order
    # @param[in] fp File pointer to the result file
    def print_tree(self, fp):
        self.__inorder_recursive(self.__root, fp)
