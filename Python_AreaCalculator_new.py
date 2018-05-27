"""This program is created by Areum. """

print "The calculator is starting now!"

name = raw_input("What's your name?: ")
option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C': 
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius ** 2
elif option == 'T': 
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print str(area)
else: 
  print "You just entered an invalid shape."
print "This program is existing..."