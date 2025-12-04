#import sys

#print(sys.argv)
#print(sys.argv[0]) # program name
#print(sys.argv[1]) # first arg


#a = 23
#b = 34
#if a == 34 or b == 34:
#    print(a + b)


a = 23
b = 34
if a == 34 and b == 34:
     print (a + b)


temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)



temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)


print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")

print("temperatures and facts about the moon".title())


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))


print("The Moon And The Earth".lower())


print("The Moon And The Earth".upper())


temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])


mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)


  print("-60".startswith('-'))

if "30 C".endswith("C"):
print("This temperature is in Celsius")


print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))


text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)


text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)