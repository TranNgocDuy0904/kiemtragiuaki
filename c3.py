def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1): 
        swapped = False 
        print(f"\nBước {i + 1}:")  
        print("Trạng thái ban đầu:", arr)
        
        for j in range(n - 1 - i):  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
            print("  Sau khi so sánh", arr[j], "và", arr[j + 1], "->", arr)
        
        if not swapped:  
            print("\nKhông có hoán đổi, dừng thuật toán sớm.")
            break


arr = list(map(int, input("Nhập dãy số nguyên, cách nhau bởi dấu cách: ").split()))

print("\nBắt đầu quá trình sắp xếp:")
bubble_sort(arr)

print("\nDãy số sau khi sắp xếp:", arr)
