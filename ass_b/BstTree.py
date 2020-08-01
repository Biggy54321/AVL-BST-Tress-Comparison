# @brief This class holds the fields required for a single node in BST
class BstNode:
    # @brief This function initializes the class object
    # @param[in] key Key of the node
    # @param[in] value Value of the node
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
        self.left = None
        self.right = None

# @brief This class manages provides an Dictionary ADT using BST
class BstTree:
    # @brief This function initializes the class object
    def __init__(self):
        self.__root = None

    # @brief This function recursively inserts a key value pair in the tree
    # @param[in] root Node pointer or object
    # @param[in] key Key to be inserted
    # @param[in] value Value to be inserted
    # @retval Node pointer or object
    def __insert_recursive(self, root, key, value):
        # Check if root is null
        if not root:
            return BstNode(key, value)
        # If key is less than current key
        elif key < root.key:
            root.left = self.__insert_recursive(root.left, key, value)
        # If key is greater than current key
        else:
            root.right = self.__insert_recursive(root.right, key, value)
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
