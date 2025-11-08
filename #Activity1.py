#Activity1
a= 10
b=12
c=0

if a and b and c:
    print("ALL THE NUMBERS HAVE BOOLEAN VALUE AS TRUE")
else:
    print("Atleast one number has boolen value as false")

    
a=10
b=-10
c=0

if a > 0 or b >0:
    print("Either of the number is greater than 0")
else:
    print("no number is greater than 0")

if b > 0 or c>0:
    print("either ofthe number is greater than 0")
else:
    print("no number is greater than 0") 

a = 10
b = 12
c = 12

print(a !=b)
print(b != c)


a = "python"
b = "coding"

if a != b:
    print(a, 'and', b, 'are different.')

a = 4
b =5 

if(a == 1) != (b==5):
    print('hello')    




height= 160
weight= 62

BMI =weight / (height/100)**2

print("your BMI is", BMI)

if BMI <= 18.4:
    print("you are underweight.")
elif BMI <= 24.9:
   print("you are healthy")
elif BMI <= 29.9:
   print("you are overweight")
elif BMI <= 34.9:
   print("you are severely overweigSht")
elif BMI <= 39.9:
   print("you are obese")
else:
   print("you are severely obese.")


