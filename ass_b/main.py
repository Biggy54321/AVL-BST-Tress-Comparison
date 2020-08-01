import re
import sys
import time
from BstTree import BstTree
from AvlTree import AvlTree

# Debug printing
print("Processing the input files...")

# Open the data file
data = open("data.txt", "r")
# Open the stop words file
stop = open("stop_words.txt", "r")

# Read the data file
data_lines = data.read().lower()

# Read the stop words
stop_words = stop.readlines()
# Remove newline from each word (list of words)
stop_words = [each.strip().lower() for each in stop_words]

for word in stop_words:
    data_lines = re.sub(r"\b{}\b".format(word), "", data_lines)

# Convert the string file in list of lines where each line is a string
data_lines = data_lines.split('\n')

# Extract only letter words from each line delimited by a non letter character
data_lines = [re.findall(r"[a-z]+", each) for each in data_lines]

# Debug printing
print("Processed the input files.")

# Check for the type of the tree
if len(sys.argv) != 2:
    print("** Program usage: python3 main.py AVL/BST")
    sys.exit()

if sys.argv[1] == "AVL":
    tree = AvlTree()
elif sys.argv[1] == "BST":
    tree = BstTree()
else:
    print("** Invalid argument: AVL or BST are the only valid arguments")
    sys.exit()

# Set current line number to zero
line_number = 0

# Debug printing
print("Beginning insertion in the {} tree...".format(sys.argv[1]))

# Get the time before execution
start_time = time.time()

# For each line insert its words in the tree
for line in data_lines:
    # For each word in that line insert that in the tree
    for word in line:
        # Find and update, if found then continue else insert new word
        if not tree.find_and_update(word, line_number):
            tree.insert(word, line_number)
    line_number += 1

# Get the time after execution
end_time = time.time()

# Debug printing
print("Finished insertion in the {} tree (TIME TAKEN {} secs).".format(sys.argv[1], end_time - start_time))


# Debug printing
print("Writing the result to the text file...")

# Write the result in the file
if sys.argv[1] == "AVL":
    result_file = open("avl_result.txt", "w")
else:
    result_file = open("bst_result.txt", "w")

# Print the tree
tree.print_tree(result_file)

# Close all files
data.close()
stop.close()
result_file.close()

# Debug printing
if sys.argv[1] == "AVL":
    print("Result written to the file <avl_result.txt>.")
else:
    print("Result written to the file <bst_result.txt>.")
