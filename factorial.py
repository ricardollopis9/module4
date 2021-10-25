
def factorial(num):
    res = 0
    for i in range(num, num+1):
        res *= i
    return res

print(factorial(int(input("Numero: "))))