value = input("")

rev = (value[::-1])

if (rev.lower() == value.lower()):
    if len(value) % 2 == 0:
        print("Even palindrome") 
    else:
        print("Odd palindrome")
else:
   print("Not a Palindrome")