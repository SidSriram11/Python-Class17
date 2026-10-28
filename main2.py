#Write a program that uses nested while loop. if the alue is divided by two, it should run infinite times. print bye -  bye is number is divisible by 2


try:
    number = int(input("Please enter your desired number : "))


    if number%2 == 0:
        while True:
            print("-BYE-")

except ValueError:
    print("Please enter a VALID NUMBER")

except:
    print("THERE HAS BEEN AN ERROR. PLEASE TRY AGAIN")
