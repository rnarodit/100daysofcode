#Write your code below this line 👇



def prime_checker (number):
    prime = True
    if (number == 1 or number == 0):
        print ("This is not prime number")
    else:
        for divide in range ( 2, number+1 ):
            if (number % divide == 0 and not divide == number):
                prime = False
        if prime == True :
            print("This is a prime number")
        else :
            print("This is not a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



