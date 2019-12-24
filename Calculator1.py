##this file is combined of vsa.py and calculator.py to be uploaded :) <3
#global Variable
numlist = []
i = 1
lennum = 1
su = 0
diff = 0 
multi = 1
divi = 1 
result = 0
operation1 = ""
#global var
pi = 22/7
def ask_pi():# pi value is different depending on question :P
    global pi
    while True:
        try:
            opt = input("Enter 1 for pie as 22/7 or 2 for 3.14, 3 for 3.14159265359 ")
            if opt == "1":
                pi = 22/7
                break
            elif opt == "2":
                pi = 3.14
                break
            elif opt == "3":
                pi = 3.14159265359
                break
            else:
                print("Enter a valid option!")
                continue
        except:
            print("Enter a valid option!")
            continue

def ask_radius(): #asks for radius 
    while True:
        try:
            radius = int(input("Enter a radius: "))
            return radius
            break
        except EOFError:
            print("Enter a valid option")
            continue
        except:
            print("Enter a number")
            continue

def ask_height(): #height is being asked in this func
    while True:
        try:
            height = int(input("Enter a height: "))
            return height
            break
        except EOFError:
            print("Enter a valid option")
            continue
        except:
            print("Enter a number")
            continue

def side_ask(): #side for cube and sqaure
    while True:
        try:
            side = int(input("Enter a side: "))
            return side
            break
        except EOFError:
            print("Enter a valid option")
            continue
        except:
            print("Enter a number")
            continue


def lbh_ask(dimension): #depending on the dimension rectangle or cuboid
    if dimension == "2d":
        while True:
            try:
                length = int(input("Enter length"))
                breadth = int(input("Enter breadth"))
                return length, breadth
            except EOFError:
                print("Enter a valid option")
                continue
            except:
                print("Enter a number")
                continue
    elif dimension == "3d":
        while True:
            try:
                length = int(input("Enter length"))
                breadth = int(input("Enter breadth"))
                height = int(input("Enter height"))
                return length, breadth, height
            except EOFError:
                print("Enter a valid option")
                continue
            except:
                print("Enter a number")
                continue
def triangle_ask(): # this is used to avoid large codes in the triangle func
    while True:
        try:
            triagle_side1 = int(input("Enter a Side1: "))
            triagle_side2 = int(input("Enter a Side2: "))
            triagle_side3 = int(input("Enter a Side3: "))
            return triagle_side1, triagle_side2, triagle_side3
            break
        except EOFError:
            print("Enter a valid option")
            continue
        except:
            print("Enter a number")
            continue


def shape_ques(dimension):# asks area and perimeter or tsa, csa ,volume (depending on dimension)
    if dimension =="2d":
        while True:
            try:
                shape_ques = int(input("Enter 1 for perimeter 2 for area: "))
                return shape_ques
            except EOFError:
                print("Enter a valid option")
                continue
            except:
                print("Enter a number")
                continue
    elif dimension == "3d":
        while True:
            try:
                shape_ques = int(input("Enter 1 for Volume, 2 for Tsa, 3 for Csa: "))
                return shape_ques
            except EOFError:
                    print("Enter a valid option")
                    continue
            except:
                print("Enter a number")
                continue


class Circle():
    """docstring for Circle
    calculates area and circumfernce"""
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi
        print(f"the circle has a radius of {self.radius}")
    def area(self):
        return self.pi * self.radius**2
    def circumfence(self):
        return 2 * self.pi * self.radius

class Sqaure():
    """docstring for Sqaure
    calculates area and perimeter"""
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4 * self.side


class Rectangle():
    """docstring for Rectangele
    calculates area and perimeter"""
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth
    def area(self):
        return self.l * self.b
    def perimeter(self):
        return 2*(self.l + self.b)


class Triangle():
    """docstring for Triangle
    calculates area and perimeter"""
    def __init__(self, side1, side2, side3):
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    def area(self):
        s = (self.s1 + self.s2 + self.s3)/2
        return (s*(s-self.s1)*(s-self.s2)*(s-self.s3))**(1/2) 


class Cuboid():
    """docstring for Cuboid
    calculates volume, tsa and csa"""
    def __init__(self, length, breadth, height):
        self.l = length
        self.b = breadth
        self.h  = height
    def volume(self):
        return self.l * self.b * self.h
    def tsa(self):
        return 2*(self.l*self.b + self.l*self.h + self.b*self.h)
    def lsa(self):
        return 2* self.h * (self.l + self.b)


class Cube():
    """docstring for Cube
    calculates volume, tsa and csa"""
    def __init__(self, side):
        self.side = side
    def volume(self):
        return self.side**3
    def tsa(self):
        return 6 * self.side
    def lsa(self):
        return 4 * self.side


class Sphere():
    """docstring for sphere
    calculates volume, tsa and csa"""
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi
    def volume(self):
        return 4/3 * self.pi * self.radius**3
    def tsa(self):
        return 4* self.pi * self.radius**2
    def csa(self):
        return 4* self.pi * self.radius**2


class Hemisphere():
    """docstring for Hemisphere
    calculates volume, tsa and csa"""
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi
    def volume(self):
        return 2/3 * self.pi * self.radius**3
    def tsa(self):
        return 3* self.pi * self.radius**2
    def tsa(self):
        return 2* self.pi * self.radius**2


class Right_Circular_Cylinder():
    """docstring for Cylinder
    calculates volume, tsa and csa"""
    def __init__(self, radius, pi, height):
        self.radius = radius
        self.pi = pi
        self.h = height
    def volume(self):
        return self.pi * self.radius**2 * self.h
    def tsa(self):
        return 2* self.pi * self.radius*(self.radius + self.h)
    def csa(self):
        return 2* self.pi * self.radius* self.h


#if __name__ == '__main__': this is of the file Vsa.py (volume surface area)
#   ask_pi()
#   hemisphere_obj = Hemisphere(10, pi)
#   shape_ans = hemisphere_obj.volume()
#   print(f"The ans is {shape_ans}")
## resets the value of all variables incase the calculator is run again
def recall():
    global numlist
    global i 
    global lennum
    global su
    global diff
    global multi
    global divi
    global result
    global operation1
    numlist = []
    i = 1
    lennum = 1
    su = 0
    diff = 0 
    multi = 1
    divi = 1 
    result = 0
    operation1 = ""

# take input for the calculator
def multiple_input():
    global lennum
    global numlist
    global i
    while True:
        try:
            lennum = int(input("How many number do want to operate with: "))
            if lennum < 2:
                print("How can you operate with one or no num?")
                continue
            elif lennum > 15:
                print("Isn't that quite a lot?")
                continue
            break
        except:
            print("Didn't I ask for a NUMBER!")
            continue
    while i <= lennum:
        try:
            numlist.append(int(input(f"enter num{i}: ")))
            i+=1
        except:
            print("YOU CAN ONLY OPERATE WITH NUMBERS!")

# calculator class takes the num list
class SimpleCalculator:
    """Can add, substract, multiply or divide multiple number """

    def __init__(self, number):
        self.nums = number

    def add_num(self):
        global su
        su = 0
        for x in self.nums:
            su+=x
        return su

    def substract_num(self):
        global diff
        diff = 0
        for x in self.nums:
            if x == self.nums[0]:
                diff = x-diff
            else:
                diff = diff - x
        return diff

    def multiply_num(self):
        global multi
        multi = 1
        for x in self.nums:
            multi*=x
        return multi


    def divide_num(self):
        global divi
        divi = 1
        for x in self.nums:
            if x == self.nums[0]:
                divi = x / divi
            else:
                divi = divi / x
        return divi

# takes the class which had taken the numbers and call the function in the class 
def operator_run(object, operator):
    while True:
        global result
        result = 0
        if operator == "*":
            result = object.multiply_num()
            print(result)
            break
        elif operator == "/":
            result = object.divide_num()
            print(result)
            break
        elif operator == "+":
            result = object.add_num()
            print(result)
            break
        elif operator == "-":
            result = object.substract_num()
            print(result)
            break
# asks for the operator and then returns it;
def operator_ask():
    while True:
        try:
            operator = input("*, /, +, - : ")
            if operator == "*" or operator == "/" or operator == "+" or operator == "-":
                return operator
            else:
                print("Enter a valid operator")
                continue
        except:
            continue

# asks for the shape and calls the particular shape function
def ask_shape():
    print("Which Shape do you want to operate")
    while True:
        try:
            shape = int(input("1 for Circle\n2 for sqauare\n3 for rectangle\n4 for triangle\n5 for cuboid\n6 for cube\n7 for sphere\n8for hemisphere\n9 for right circular cylinder\n"))#10 for right circular cone: "))
            if shape == 1:
                return circle()
            elif shape == 2:
                return sqauare()
            elif shape == 3:
                return rectangle()
            elif shape == 4:
                return triangle()
            elif shape == 5:
                return cuboid()
            elif shape == 6:
                return cube()
            elif shape == 7:
                return sphere()
            elif shape == 8:
                return hemisphere()
            elif shape == 9:
                return right_circular_cylinder()
            else:
                print("That shape does not exist")
        except EOFError:
            print("lol")
            continue
        except ValueError:
            print("lol")
            continue
    return

########
# shape func
# find the ###### for the end :)

def circle():  #circle
    global pi
    radius = ask_radius()
    ask_pi()
    shape_que = shape_ques("2d")
    if shape_que == 1:
        circle_obj = Circle(radius, pi)
        shape_ans = circle_obj.circumfence()
        print(f"The perimeter is {shape_ans}")
    elif shape_que == 2:
        circle_obj = Circle(radius,pi)
        shape_ans = circle_obj.area()
        print(f"The area is {shape_ans}")
    else:
        circle()

def sqauare():
    side = side_ask()
    shape_que = shape_ques("2d")
    if shape_que == 1:
        sqaure_obj = Sqaure(side)
        sqaure_ans = sqaure_obj.perimeter()
        print(f"The perimeter is {sqaure_ans}")
    elif shape_que == 2:
        sqaure_obj = Sqaure(side)
        sqaure_ans = sqaure_obj.area()
        print(f"The area is {sqaure_ans}")
    else:
        sqaure()
    pass


def rectangle():
    l, b = lbh_ask("2d")
    shape_que = shape_ques("2d")
    if shape_que == 1:
        rectangle_obj = Rectangle(l, b)
        shape_ans = rectangle_obj.perimeter()
        print(f"The perimeter is {shape_ans}")
    elif shape_que == 2:
        rectangle_obj = Rectangle(l, b)
        shape_ans = rectangle_obj.area()
        print(f"The area is {shape_ans}")
    else:
        rectangle()


def triangle():
    triagle_side1, triagle_side2, triagle_side3 = triangle_ask()
    shape_que = shape_ques("2d")
    if shape_que == 1:
        triangle_obj = Triangle(triagle_side1, triagle_side2, triagle_side3)
        triangle_ans = triangle_obj.perimeter()
        print(f"The perimeter is {triangle_ans}")
    elif shape_que == 2:
        triangle_obj = Triangle(triagle_side1, triagle_side2, triagle_side3 )
        triangle_ans = triangle_obj.area()
        print(f"The area is {triangle_ans}")
    else:
        triangle()


def cuboid():
    l, b, h = lbh_ask("3d")
    shape_que = shape_ques("3d")
    if shape_que == 1:
        cuboid_obj = Cuboid(l, b,h )
        shape_ans = cuboid_obj.volume()
        print(f"The volume is {shape_ans}")
    elif shape_que == 2:
        cuboid_obj = Cuboid(l, b,h)
        shape_ans = cuboid_obj.tsa()
        print(f"The TSA is {shape_ans}")
    elif shape_que == 3:
        cuboid_obj = Cuboid(l, b,h)
        shape_ans = cuboid_obj.csa()
        print(f"The CSA is {shape_ans}")
    else:
        cuboid()

    pass


def cube():
    side = side_ask()
    shape_que = shape_ques("3d")
    if shape_que == 1:
        cube_obj = Cube(side)
        shape_ans = cube_obj.volume()
        print(f"The volume is {shape_ans}")
    elif shape_que == 2:
        cube_obj = Cube(side)
        shape_ans = cube_obj.tsa()
        print(f"The TSA is {shape_ans}")
    elif shape_que == 3:
        cube_obj = Cube(side)
        shape_ans = cube_obj.csa()
        print(f"The CSA is {shape_ans}")
    else:
        cube()
    pass


def sphere():
    global pi
    radius = ask_radius()
    ask_pi()
    shape_que = shape_ques("3d")
    if shape_que == 1:
        sphere_obj = Sphere(radius, pi)
        shape_ans = sphere_obj.volume()
        print(f"The volume is {shape_ans}")
    elif shape_que == 2:
        sphere_obj = Sphere(radius, pi)
        shape_ans = sphere_obj.tsa()
        print(f"The Tsa is {shape_ans}")
    elif shape_que == 3:
        sphere_obj = Sphere(radius, pi)
        shape_ans = sphere_obj.csa()
        print(f"The Csa is {shape_ans}")
    else:
        sphere()


def hemisphere():
    global pi
    radius = ask_radius()
    ask_pi()
    shape_que = shape_ques("3d")
    
    if shape_que == 1:
        hemisphere_obj = Hemisphere(radius, pi)
        shape_ans = hemisphere_obj.volume()
        print(f"The volume is {shape_ans}")
    elif shape_que == 2:
        hemisphere_obj = Hemisphere(radius, pi)
        shape_ans = hemisphere_obj.tsa()
        print(f"The Tsa is {shape_ans}")
    elif shape_que == 3:
        hemisphere_obj = Hemisphere(radius, pi)
        shape_ans = hemisphere_obj.csa()
        print(f"The Csa is {shape_ans}")
    else:
        hemisphere()
        
    pass


def right_circular_cylinder():
    global pi
    radius = ask_radius()
    ask_pi()
    height = ask_height()
    shape_que = shape_ques("3d")
    if shape_que == 1:
        cylinder_obj = Right_Circular_Cylinder(radius, pi,height)
        shape_ans = cylinder_obj.volume()
        print(f"The Volume is {shape_ans}")
    elif shape_que == 2:
        cylinder_obj = Right_Circular_Cylinder(radius, pi,height)
        shape_ans = cylinder_obj.tsa()
        print(f"The Tsa is {shape_ans}")
    elif shape_que == 3:
        cylinder_obj = Right_Circular_Cylinder(radius, pi,height)
        shape_ans = cylinder_obj.csa()
        print(f"The Csa is {shape_ans}")
    else:
        right_circular_cylinder()
#end of shape funcs
##########

if __name__ == '__main__':   #incase of module import
    print("Welcome to RuDra's calculator \nWARNING: It might have some bugs, sorry :)")
    try:
        input("press Enter key to continue: ")
    except:
        pass

    print("Do you want to use a simple calculator(/ * + -) or Use go for Volumes and Areas") #ask whether use calculator or volumes
    while True:
        recall()
        try:
            operation = input("Enter 1 for simple calculator, 2 for Volumes and Areas(Enter Z to quit): ").upper()
            if operation == "1":
                print("Would you like to multiply(*), divide(/), add(+) or substract(-): ")
                operator = operator_ask() # operator input
                multiple_input() #input list
                obj = SimpleCalculator(numlist)
                operator_run(obj,operator)

            elif operation == "2":
                ask_shape()
            
                
            elif operation == "Z": #quit
                print("OK Cya!")
                break
            else:
                print("Enter a valid option")
        except EOFError: # enter ^z in cmd causes this error 
            print("Try again")
        except:
            print("GOTCHA error")
            