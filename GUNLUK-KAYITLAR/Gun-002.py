print("Welcome to the bmi calculator\n")
name = input("What is your name? ")
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    bmi = (weight)/((height/100)**2)

    if bmi>0:
        if(bmi < 18.5):
            print(f"{name}, you are underweight. Your bmi is {round(bmi, 2)}")
        elif(bmi <= 24.9):
            print(f"{name}, you are normal weight. Your bmi is {round(bmi, 2)}")
        elif(bmi < 29.9):
            print(f"{name}, you are overweight. Your bmi is {round(bmi, 2)}")
        elif(bmi < 34.9):
            print(f"{name}, you are severely obese bro. Your bmi is {round(bmi, 2)} be careful with your health")
        else:
            print(f"{name}, you are morbidly obese. Your bmi is {round(bmi, 2)}")
    else:
        print("Enter valid input")
except ValueError:
    print("Invalid character! Please enter numbers only")
