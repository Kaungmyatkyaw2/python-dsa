from Searchalgo.linearSearch import LinearSearch

array = LinearSearch([1, 2, 3, 4, 5, 6, 7])

# Worse Case
print(f"Index for 50 : {array.findItem(50)}")

# Average Case
print(f"Index for 4  : {array.findItem(4)}")

# Best Case
print(f"Index for 1  : {array.findItem(1)}")

# worse case : O(n)
