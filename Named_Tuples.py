#Adapted from https://ceasarjames.wordpress.com/2012/03/19/how-to-use-default-arguments-with-namedtuple/

 

from collections import namedtuple

 

# Define Class Car Descriptor using namedtuple

#

# class will have objects used, color, and mileage

class Car_Descriptor(namedtuple('Car_Descriptor', 'used color mileage')):

                # Define the 'new' contructor to have default values of:

                #             boolean False for used

                #             int 0 for mileage

                def __new__(cls, color, used=False, mileage=0):

                                # Return to the super class the constructor just described

                                return super(Car_Descriptor, cls).__new__(cls, color, used, mileage)

 

car_1 = Car_Descriptor("orange")

print("car_1 = Car_Descriptor(\"orange\"):\n" + str(car_1))

 

car_2 = Car_Descriptor("orange", mileage=0.00)

print("\ncar_2 = Car_Descriptor(\"orange\", mileage=0.00):\n" + str(car_2))

 

car_3 = Car_Descriptor("orange", True)

print ("\ncar_3 = Car_Descriptor(\"orange\", True):\n" + str(car_3) + "\n")

 

print("""

for car in [car_1, car_2, car_3]:

                for _ in car:

                                print(_)""")

for car in [car_1, car_2, car_3]:

                for _ in car:

                                print(_)

