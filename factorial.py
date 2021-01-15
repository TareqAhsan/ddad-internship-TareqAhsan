num = int(input())
fact = 1

if num > 0 and num < 10:
    
 while (num > 0):
    fact = fact * num
    num = num - 1
    
 print(fact)

else:
    print("out of range")
