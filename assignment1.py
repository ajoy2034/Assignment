def prime_finder(n):
    if n<1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
               return False

    return
number=(int(input("Enter any number:")))
if prime_finder(number):
    print(f"{number} is a prime")
else:
    print(f"{number} is not a prime")