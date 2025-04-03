def fibonacci(n):
    if n < 0:
        return "Lỗi: n phải là số nguyên không âm!"
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev2, prev1 = 0, 1  # F(0) = 0, F(1) = 1
    for _ in range(2, n + 1):
        current = prev1 + prev2  # Tính Fibonacci hiện tại
        prev2, prev1 = prev1, current  # Cập nhật hai số trước
    
    return prev1

# Nhập số nguyên không âm từ người dùng
while True:
    try:
        n = int(input("Nhập số nguyên n (≥ 0): "))
        if n >= 0:
            break
        print("Vui lòng nhập số nguyên không âm!")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

# In kết quả
print(f"Số Fibonacci thứ {n} là:", fibonacci(n))
