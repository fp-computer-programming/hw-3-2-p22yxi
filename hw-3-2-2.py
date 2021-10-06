# Author : Yongdong Xi (Oct 3 2021)

BMI = float(input("what is the BMI of this person"))

if BMI > 40:
    print("he or she is Extremely Obese")
elif BMI >= 30:
    print("he or she is Obese")
elif BMI >= 25:
    print("he or she is Overweight")
elif BMI >= 20:
    print("he or she is  Healthy")
elif BMI < 20:
    print("he or she is Underweight")
