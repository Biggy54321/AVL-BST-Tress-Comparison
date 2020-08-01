import time
from Avl import AvlTree
from Bst import BstTree

# Open the test file with keywords (no meanings are inserted for testing)
# The keywords are sorted to test the search times in AVL and BST Dictionary ADT
key_words_file = open("test", "r")

# Read the words from the file
key_words = key_words_file.readlines()

# Remove newline character from each word
key_words = [word.strip() for word in key_words]

# Create an AVL and BST Tree
avl = AvlTree()
bst = BstTree()

# Insert each keyword in both the tree (for testing no meaning is inserted)
for word in key_words:
    avl.insert(word, "AVL-tree-key-found")
    bst.insert(word, "BST-tree-key-found")

# Get the start time before searching in AVL
st_time = time.time()
# Search for the last keyword of the test file
print(avl.search("lysates"))
# Get the ending time after searching in AVL
en_time = time.time()
# Print the time required for searching a keyword in AVL
print("** Time for AVL search", (en_time - st_time) * 1000, "milli secs", end="\n\n")

# Get the start time before searching in BST
st_time = time.time()
# Search for the last keyword of the test file
print(bst.search("lysates"))
# Get the ending time after searching in BST
en_time = time.time()
# Print the time required for searching a keyword in BST
print("** Time for BST search", (en_time - st_time) * 1000, "milli secs", end="\n\n")

# Close the file
key_words_file.close()

# Print the conclusion
print("INFERENCE: Hence in case of height balanced tree the time required to search for a key is O(lg(n)) and in case of binary search tree the time required is O(n), so maximum number of comparison that may require in case of height balanced is again O(lg(n)), while in case of binary search tree is O(n)")
