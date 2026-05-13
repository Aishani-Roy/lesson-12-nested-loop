lower=int(input("enter your lower range:"))
upper=int(input("enter your upper range:"))
print("the prime numbers from ",lower,"to",upper,"is:")
for number in range(lower,upper+1):
    for denominator in range(2,number):
        if number%denominator==0:
            break
    else:
        print(number,end=" ")    
