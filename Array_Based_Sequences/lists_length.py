import sys  # provides the getsizeof function

# Code Fragment 5.1
# data = []

# for i in range(26):
#     a = len(data)
#     b = sys.getsizeof(data)     # actual size in bytes
#     print(f"Length: {a:3d}; Size in bytes: {b:4d}")
#     data.append(None)   # increasize the length by one

# R-5.2
# data = []

# original = None
# for i in range(1000):
#     a = len(data)
#     b = sys.getsizeof(data)     # actual size in bytes

#     if original != b:
#         print(f"Length: {a:3d}; Size in bytes: {b:4d}")
#         original = b

#     data.append(None)   # increasize the length by one

# R-5.3
data = [None] * 100     # initial list with size 100
data_len = len(data)

for i in range(data_len):
    a = len(data)
    b = sys.getsizeof(data)

    print(f"Length: {a:3d}; Size in bytes: {b:4d}")

    data.pop()  # remove an element 
    