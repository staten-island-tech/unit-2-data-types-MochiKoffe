""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values: 
    print(i)

print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it")
if day_of_week == "Friday": 
    print("correct")
else: 
    print("incorrect") """

""" number = int(input("give me number"))

if number >= 21: 
    print("can vote and gamble")
elif(number >= 18): 
    print("can vote but not gamble")
else: 
    print("have a juicebox kid") """

""" temp = 55
if (temp > 40 and temp < 60):
    print("lightjacket needed")
elif (temp <20 or temp > 90): 
    print("extreme") """

""" def discount(isMember, age, isResident):
    if (isMember or isResident):
        print("discount granted")
age = int(input("enter age"))
if age >= 65:
    print("discount granted")
elif(age < 12): 
    print("discount granted")
else: 
    print("NO DISCOUNT") """

""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68: 
    print("warm")
elif temp == 68: 
    print("perfect")
else: 
    print("cold") """

""" bill = float(input("enter bill"))
tip = float(input("how much is your tip"))
if bill > 0:
    print(tip)
if tip >= 0:
    print(bill*tip+bill) """


bill = int(input("what bill"))
service = input("good, bad, great, okay")
def getTip(bill, service):
    if bill >= 0:
        print(service)
    if service == "great":
        print(float(.25))
    elif service == "bad":
        print(float(0))
    elif service == "okay":
        print(float(.15))
    elif service == "good":
        print(float(.2))

""" number = int(input("type a number"))
if number % 2 == 0: 
    print("even")
else:
    print("odd") """