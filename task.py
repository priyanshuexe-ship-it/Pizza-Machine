print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()

bill_calculator = 0
if size == "S" or size == "M" or size == "L":

    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
    if pepperoni == "Y" or pepperoni == "N":
        extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
        if extra_cheese== "Y" or extra_cheese == "N":
            if size == "S":
                bill_calculator += 15
                if pepperoni == "Y":
                    bill_calculator += 2
            elif size == "M":
                bill_calculator += 20
                if pepperoni == "Y":
                    bill_calculator += 3
            elif size == "L":
                bill_calculator += 25
                if pepperoni == "Y":
                    bill_calculator += 3
            if extra_cheese == "Y":
                bill_calculator += 1
            print(f"Your total bill = {bill_calculator} visit again")
        else:
            print("Oops! Type Error. Type correctly for cheese")
    else:
        print("Oops! Type Error. Type correctly for pepperoni")

else:
    print("Oops! Type Error. Type correct Size")