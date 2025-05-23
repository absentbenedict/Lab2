def calculate_bmi(weight,height,cls):
    bmi = weight / (height**2)
    if bmi < 18.5:
        cls =-1
    elif 18.5<bmi<25:
        cls = 0
    else:
        cls = 1
    
    return bmi , cls

def get_user_input():
    weight = float(input("Please input your weight in kg :"))
    height = float(input("Please input your height in m: "))
    return weight , height

if __name__ == "__main__":
    weight , height = get_user_input()
    bmi , cls = calculate_bmi(weight , height)
    print("Your BMI is:" , bmi) 
    if cls == -1:
        print("You are underweight")
    elif cls == 0 :
        print("Your weight is normal")
    elif cls == 1:
        print("You are overweight")