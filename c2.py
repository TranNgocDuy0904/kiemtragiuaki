import math 
def factorial(n):
    result = 1
    for i in range(1, n + 1): 
        result *= i
    return result

while True:
    try:
        n = int(input("Nhập một số nguyên không âm: "))
        if n < 0:
            print("Vui lòng nhập một số nguyên không âm!")
        else:
            break
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")


print(f"{n}! = {factorial(n)}")


print(f"Kiểm tra với thư viện: {n}! = {math.factorial(n)}")
