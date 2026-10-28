try:
    numerator = int(input("Please enter your desired numerator : "))
    denominator = int(input("Please enter your desired denominator : "))

    final_fraction = numerator/denominator
    print(final_fraction)

except ZeroDivisionError:
    print("Please enter a denominator that is NOT ZERO.")

except ValueError:
    print("Please enter a VALUE that is an INTEGER.")

except:
    print("There has been an ERROR. Please try again.")

else:
    print("I am inside else block")

finally:
    print("I am inside the finally block")