def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True

while True:
    try:
        n = int(input("Nhập một số nguyên dương: "))
        if n <= 0:
            print("Vui lòng nhập một số nguyên dương lớn hơn 0!")
        else:
            break
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

if is_prime(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
