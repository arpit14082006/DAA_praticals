# Linear Search

arr = [12, 45, 67, 23, 89, 34]
target = 23

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:", i)
        found = True
        break

if found == False:
    print("Element not found")