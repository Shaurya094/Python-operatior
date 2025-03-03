h = float(input("What is your height?"))
w = float (input("What is your weight?"))
b = int(w/(h/100)**2)

print ("Your BMI is", b)
# 18.9, 29.9, 34.9, 39.9
if b <= 18.9:
    print ("your are underweight.")
elif b <=24.9:
    print ("you are healthy.")
elif b <=39.9:
    print ("you are overweight.")
elif b <=34.9:
    print ("you are serverly overweight.")
elif b <=39.9:
    print ("you are obese.")
else:
    print ("you are serverly obese.")