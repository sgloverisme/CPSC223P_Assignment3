from mathmatics.geometry.circle import circumference
from mathmatics.geometry.circle import area
from mathmatics.geometry.cube import surface_area
from mathmatics.geometry.cube import volume
from mathmatics.geometry.rectangle import perimeter

#circle  -- working
print("printing circle values:")
print(circumference(3))
print(area(3))

#cube --wokring
print("printing cube values:")
print(surface_area(4))
print(volume(5))

#rectangle -- working
from mathmatics.geometry.rectangle import area
print("printing rectangle values:")
print(perimeter(3,4))
print(area(4,4))

#whoami geo - working
from mathmatics.geometry.whoami import getname
print(getname())

#working 
from mathmatics.numbers.series import sum
print("sum: ", sum(list = [1,2,3,4,5]))

#working 
from mathmatics.numbers.series import average
print("average: ", average(list=[1,2,3,4,5]))

#working
from mathmatics.numbers.simple import addition
print("addition: ", addition(1,3))

#working
from mathmatics.numbers.simple import subtraction
print("subtraction: ", subtraction(4,2))

#working
from mathmatics.numbers.simple import multipulication
print("multi: ", multipulication(3,2))

#working
from mathmatics.numbers.simple import division
print("division: ", division(4,2))

#working
from mathmatics.numbers.whoami import getname
print(getname())