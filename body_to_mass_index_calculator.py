person_1 = "JR"
height_1_m = 2
weight_1_kg = 98

person_2 = "JR's bitch"
height_2_m = 1.7
weight_2_kg = 60

person_3 = "JR's supplier"
height_3_m = 1.9
weight_3_kg = 120

person_4 = "JR's accountant"
height_4_m = 2
weight_4_kg = 40


def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)
    print("bmi: " + str(bmi))
    if 18.5 <= bmi <= 25:
        return name + " not  overweight"
    elif bmi < 18.5:
        return name + " underweight"
    else:
        return name + " overweight"


result1 = bmi_calculator(person_1, height_1_m, weight_1_kg)
result2 = bmi_calculator(person_2, height_2_m, weight_2_kg)
result3 = bmi_calculator(person_3, height_3_m, weight_3_kg)
result4 = bmi_calculator(person_4, height_4_m, weight_4_kg)

print(result1)
print(result2)
print(result3)
print(result4)