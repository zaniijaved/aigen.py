# Problem_no 1
# calculate your age based on the current year and yoyr birth year
def agecalculator()-> int:
    birth_year:int = int(input("Enter your Birth-Year = "))
    current_year:int = int(input("Enter your Current-Year = "))
    print("Your age is = ",(current_year-birth_year))
    return print
output = agecalculator()
print("Your age is:", output ,"years")

#------------------------------------------------------------------
#problem_2
#a program that calculate the area of a rectangle using lenght and width variables
def areacalculator()-> float:
    lenght:int = int(input("Enter the lenght of a rectangle = "))
    width:int = int(input("Enter the width of a rectangle = "))
    print("The area of your rectangle is = lenght*width = ",lenght*width,"square unit")
    return print
outputofarea = areacalculator()
print("The area of the rectangle is:", outputofarea ,"metersquared")
#-----------------------------------------------------------------------------
#Problem_no 3
#a program that calculate the area of a circle
print("Circle area calculator")
def calculateAreaofCircle() -> float:
    radius:int = int(input("enter the radius of = "))
    pie_value:float =3.141592653589793238462643383279502884197
    print("the area of circle is = value of pie *square of radius = ", pie_value*radius**2,"square unit")
    return print
outputofarea = calculateAreaofCircle()
print("The area of the Circle is : " , outputofarea ,"metersquared")
#-------------------------------------------------------------------
#Problem_no4
#a program that calculates the area of cube
print("cube area calculator")
def calculateAreaofCube() -> float:
    variable :int = 6
    edges:int =int(input("enter number of edges here ="))
    print("the area of cube is = 6*square of edges here =",6*edges**2,"meter cube")
    return print
outputofCube = calculateAreaofCube()
print("The area of the Cube is : " , outputofCube , "metercube")


#-------------------------------------------------------------------------------
#Problem-no5 (a)
# program that converts temperature from celcius to fahrenheit
print("temperature convertor program")
def convertTemperature() -> float:
    temperature:float = float(input("Enter the temperature in Celsius: "))
    result:float = (temperature * 9/5) + 32
    return result
outputOfTemperature = convertTemperature()
print("The temperature in Fahrenheit is: ", outputOfTemperature , " degrees")
#----------------------------------------------------------------------
#Problem-no5 (b)
#program that converts temperature from fahrenheit to Celsius
print("temperature convertor program")
def convertTemperatureToCelsius() -> float:
    temperature:float = float(input("Enter the temperature in Fahrenheit: "))
    result:float = (temperature - 32) * 5/9
    return result
outputOfTemperatureToCelsius = convertTemperatureToCelsius()
print ("the temperatue in celsius is : ",outputOfTemperatureToCelsius ," degrees")

#-------------------------------------------------------------------

#Problem_no6
#convert a number in seconds
print("Time Calculator")
def convertMinutesToSeconds() -> float:
    time_minutes = int(input("Enter your time in minutes = "))
    print("Time in second is = (time minutes*60) = ",(time_minutes*60) ,"sec")
    return print
outputOfMinutesToSeconds = convertMinutesToSeconds()
print("The time in seconds is: ", outputOfMinutesToSeconds , " seconds")


#--------------------------------------------------------------------------------

#Problem_7
# program that calculates the percentage
print("Percentage Calculator")
def calculatePercentage() -> float:
    percentage = int(input("Enter your percentage: "))
    marks = int(input("Enter your marks: "))
    print("Percentage is: ", ((percentage / 100) * marks))
    return print
outputOfPercentage = calculatePercentage()
print("The percentage is : " , outputOfPercentage ,"%")

#--------------------------------------------------------------------------------

#Problem-no8
# program that calculates BMI
print("BMI Calculator")
def calculateBmi() -> float:
    weight = int(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    return bmi
outputOfBmi = calculateBmi()
print("Your BMI is: ", outputOfBmi)

 #-----------------------------------------------------------------------------
 # Problem-no9
 # program that calculates the volume of cylinder
print("Cylinder Volume Calculator (V = πr²h)")
def calculateVolumeOfCylinder() -> float:
    radius = int(input("Enter your radius: "))
    height = int(input("Enter your height: "))
    pie_value = 3.1416
    print("Volume of Cylinder is: ", pie_value * (radius ** 2) * height)
    return print
outputOfCylinder = calculateVolumeOfCylinder()
print("The volume of the Cylinder is : " , outputOfCylinder , "metercube")
