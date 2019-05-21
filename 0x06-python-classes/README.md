# 0x06. Python - Classes and Objects

### Background Context

OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow. As usual, make sure you type (never copy and paste), test, and understand all examples shown in the following links (including those in the video). The biggest and most important task of this project is the reading. The project itself will not take you more than 2-3 hours if you take the time to read and understand everything.

### Resources

* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/izl1kO1isRJo6h_Ce2pmhw)(Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)
* [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/K5t1QFchQYs7rkt62uMo7A)(Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
* [Properties vs. Getters and Setters](https://intranet.hbtn.io/rltoken/LZg7XYGGZj49Gu2276afpA)
* [Learn to Program 9 : Object Oriented Programming](https://intranet.hbtn.io/rltoken/aFk7Ki8TPw5vZZBx2JXvIQ)
* [Python Classes and Objects](https://intranet.hbtn.io/rltoken/CFTUXsxbTVu4xb698_2bmQ)
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/DK1vkIQ0xT1fmMrmBcSGiA)

### MORE INFO:
**Documentation is now mandatory!** Each module, class, and method must contain docstring as comments. 
* [Example Google Style Python Docstrings](https://intranet.hbtn.io/rltoken/SYdQnrcR2jL5hIs5TkIN5Q)

##TASKS

### TASK 0
Write an empty class Square that defines a square:

* You are not allowed to import any module

File: `0-square.py`

```
guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$
```

### TASK 1
Write a class Square that defines a square by: (based on 0-square.py)

* Private instance attribute: size
* Instantiation with size (no type/value verification)
* You are not allowed to import any module

**Why?**

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

File: `1-square.py`

```
guillaume@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/0x06$
```

### TASK 2
Write a class Square that defines a square by: (based on 1-square.py)

* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
  * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
  * if size is less than 0, raise a ValueError exception with the message size must be >= 0
*You are not allowed to import any module

File: `2-square.py`

```
guillaume@ubuntu:~/0x06$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/0x06$
```

### TASK 3
Write a class Square that defines a square by: (based on 2-square.py)

* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
  * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
  * if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Public instance method: def area(self): that returns the current square area
* You are not allowed to import any module

File: `3-square.py`
```
guillaume@ubuntu:~/0x06$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/0x06$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/0x06$ 
```

### TASK 4
Write a class Square that defines a square by: (based on 3-square.py)

* Private instance attribute: size:
  * property def size(self): to retrieve it
  * property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    *if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area
* You are not allowed to import any module

**Why?**

Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignation of a private attribute and also define how this one will be available from outside (get the attribute value) - by copy? by assignation, etc. Also, adding type/value validation in the setter will centralize the logic, you will do it in only one place.

File: `4-square.py`

```
guillaume@ubuntu:~/0x06$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/0x06$
```

### TASK 5
Write a class Square that defines a square by: (based on 4-square.py)

* Private instance attribute: size:
  * property def size(self): to retrieve it
  * property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
  * if size is equal to 0, print an empty line
* You are not allowed to import any module

File: `5-square.py`

```
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/0x06$
```

### TASK 6
Write a class Square that defines a square by: (based on 5-square.py)

* Private instance attribute: size:
  * property def size(self): to retrieve it
  * property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Private instance attribute: position:
  * property def position(self): to retrieve it
  * property setter def position(self, value): to set it:
    *position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
* Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
  * if size is equal to 0, print an empty line
  * position should be use by using space - Don’t fill lines by spaces when position[1] > 0
* You are not allowed to import any module

File: `6-square.py`

```
guillaume@ubuntu:~/0x06$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/0x06$
```