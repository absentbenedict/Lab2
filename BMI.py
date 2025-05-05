def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        return -1
    elif 18.5 <= bmi < 25.0:
        return 0
    else:
        return 1


def get_user_input():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    return weight, height

if __name__ == "__main__":
    weight, height = get_user_input()
    classification = calculate_bmi(weight, height)
    
    if classification == -1:
        print("You are underweight.")
    elif classification == 0:
        print("You have a normal weight.")
    else:
        print("You are overweight.")
