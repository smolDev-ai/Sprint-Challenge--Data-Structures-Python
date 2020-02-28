import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Replace the nested for loops below with your improvements
# Runtime of this is O(n) or O(n^2) -- That said, the files both contain 10000
# items so I'm a little hesistant. My best guess is O(n).
bst = BinarySearchTree(names_1[0])
names = 1

while names <= len(names_1[1:]):
    bst.insert(names_1[names])
    names += 1


duplicates = [duplicate for duplicate in names_2 if bst.contains(duplicate)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
