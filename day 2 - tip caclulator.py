from art import logo
print(logo)

print("Welcome to the tip calculator")
bill = float(input("Enter your total amount of bill $?"))
tip = float(input("What percentage of tip you would like to give ?10 ,12 or 15\n "))
person = int(input("How many people do you want to split your bill with \n"))
total_amount = (tip/100)*bill + bill
each_person = total_amount/ person
roun = round(each_person , 2)
print(f"Each person should pay : ${roun}")