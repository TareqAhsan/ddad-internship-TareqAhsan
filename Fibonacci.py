size = int(input())
num1 = 0
num2 = 1
for i in range(size):
    print(num1)
    fibo = num1 + num2
    num1 = num2
    num2 = fibo

