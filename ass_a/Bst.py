# @brief This class holds the fields required for a single node in BST
class BstNode:
    # @brief This function initializes the class object
    # @param[in] key Key of the node
    # @param[in] value Value of the node
    def __init__(self, key, value):
        self.key = key
        self.value = value
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

