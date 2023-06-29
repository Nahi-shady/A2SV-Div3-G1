def countingSort(arr):
    # Write your code here
    count = [0]*100
    for i in arr:
        count[i] += 1
    return count