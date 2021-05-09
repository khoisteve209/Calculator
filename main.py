try:
    print("THIS IS A CONSOLE CALCULATOR")
    print("1 is addition")
    print("2 is subtraction")
    print("3 is multiplication")
    print("4 is divison")
    print("5 is %")
    print("6 is exit")
    while True:
        choice = input("Which choice: ")
        if choice == "1":
            num_1 = float(input("First number: "))
            num_2 = float(input("Second number: "))
            num_1_2  = num_1 + num_2
            print(str(num_1) + " + " + str(num_2) + " = " + str(num_1_2))
            print("choice from 1 to 6 ")
        elif choice == "2":
            num_3 = float(input("Subtrahend: "))
            num_4 = float(input("Minus: "))
            num_3_4  = num_3 - num_4
            print(str(num_3) + " - " + str(num_4) + " = " + str(num_3_4))
            print("choice from 1 to 6 ")
        elif choice == "3":
            num_5 = float(input("First factor number: "))
            num_6 = float(input("Second factor number: "))
            num_5_6  = num_5 * num_6
            print(str(num_5) + " * " + str(num_6) + " = " + str(num_5_6))
            print("choice from 1 to 6 ")
        elif choice == "4":
            num_7 = float(input("Dividend: "))
            num_8 = float(input("Divisor: "))
            num_7_8 = num_7 / num_8
            print(str(num_7) + " / " + str(num_8) + " = " + str(num_7_8))
            print("choice from 1 to 6 ")
        elif choice == "5":
            num_9 = float(input("Dividend: "))
            num_10 = float(input("Divisor: "))
            num_9_10 = num_9 % num_10
            print(str(num_9) + " % " + str(num_10) + " = " + str(num_9_10))
            print("choice from 1 to 6 ")
        elif choice == "6":
            break
        else:
            print("THE HELL")
            print("choice from 1 to 6 ")
except:
    print("Something went wrong, try again")
