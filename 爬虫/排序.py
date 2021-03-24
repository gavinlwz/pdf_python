
# def bubbleSort(arr):
#     for i in range(len(arr)-1):         # 循环第 i 趟
#         for j in range(len(arr)-i-1):   # j 为下标
#             if arr[j] > arr[j+1]:       # 如果这个数大于后面的数就交换两者的位置
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#             print(arr)
# arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
# bubbleSort(arr)

def bubble_sort(arr):
    for i in range(len(arr)-1):         # 循环第 i 趟
        flag = False
        for j in range(len(arr)-i-1):   # j 为下标
            if arr[j] > arr[j+1]:       # 如果这个数大于后面的数就交换两者的位置
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            return
        print(arr)                      # 每一趟比较完了就打印一次


arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
bubble_sort(arr)