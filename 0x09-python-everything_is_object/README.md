# 0x09. Python - Everything is object

## Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```

OK. But what about this?

```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types. The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.

Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

All your answers should be only one line in a file. No space before or after the answer.

## Resources

* [9.10. Objects and values](https://intranet.hbtn.io/rltoken/n1x09X-KJSllpJkJorBw2A)
* [9.11. Aliasing](https://intranet.hbtn.io/rltoken/3teQMNNfDeyGvCtZfjsf5g)
* [Immutable vs mutable types](https://intranet.hbtn.io/rltoken/JuPVygeoG27Q_qKxB2lP8g)
* [Mutation](https://intranet.hbtn.io/rltoken/UbL96sV3cIxewdQPW_zwRw)(Only this chapter)
* [9.12. Cloning lists](https://intranet.hbtn.io/rltoken/-t_1VsmKlgWHszL5y1YiKA)
* [Python tuples: immutable but potentially changing](https://intranet.hbtn.io/rltoken/IdBAdTYNLuS3YpRRQIam6Q)

## TASKS

### TASK 0
What function would you use to print the type of an object?

Write the name of the function in the file, without ().

### TASK 1
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

### TASK 2
In the following code, do a and b point to the same object? Answer with Yes or No.

```
>>> a = 89
>>> b = 100
```

### TASK 3
In the following code, do a and b point to the same object? Answer with Yes or No.

```
>>> a = 89
>>> b = 89
```

### TASK 4
In the following code, do a and b point to the same object? Answer with Yes or No.

```
>>> a = 89
>>> b = a
```

### TASK 5
In the following code, do a and b point to the same object? Answer with Yes or No.

```
>>> a = 89
>>> b = a + 1
```

### TASK 6
What do these 3 lines print?

```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```

### TASK 7
What do these 3 lines print?

```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```

### TASK 8
What do these 3 lines print?

```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```

### TASK 9
What do these 3 lines print?

```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```

### TASK 10
What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

### TASK 11
What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

### TASK 12
What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

### TASK 13
What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

### TASK 14
What does this script print?

```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

### TASK 15
What does this script print?

```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

### TASK 16
What does this script print?

```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

### TASK 17
What does this script print?

```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

### TASK 18
What does this script print?

```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

### TASK 19
Write a function def copy_list(l): that returns a copy of a list.

* The input list can contain any type of objects
* Your file should be maximum 3-line long (no documentation needed)
* You are not allowed to import any module

```
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
```

**No test cases needed**

### TASK 20
`a = ()`

Is a a tuple? Answer with Yes or No.

### TASK 21
`a = (1, 2)`

Is a a tuple? Answer with Yes or No.

### TASK 22
`a = (1)`

Is a a tuple? Answer with Yes or No.

### TASK 23
`a = (1, )`

Is a a tuple? Answer with Yes or No.

### TASK 24
What does this script print?

```
a = (1)
b = (1)
a is b
```

### TASK 25
What does this script print?

```
a = (1, 2)
b = (1, 2)
a is b
```

### TASK 26
What does this script print?

```
a = ()
b = ()
a is b
```

### TASK 27
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

Will the last line of this script print 139926795932424? Answer with Yes or No.

### TASK 28
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

Will the last line of this script print 139926795932424? Answer with Yes or No.

### TASK 29
Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

* introduction
* id and type
* mutable objects
* immutable objects
* why does it matter and how differently does Python treat mutable and immutable objects
* how arguments are passed to functions and what does that imply for mutable and immutable objects
If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on Twitter and LinkedIn.

When done, please add all urls below (blog post, tweet, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

### TASK 30
```
guillaume@ubuntu:/python3$ cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
guillaume@ubuntu:/python3$ 
```

Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

* How many string objects are created by the execution of the first line of the script? (106-line1.txt)
* How many string objects are created by the execution of the second line of the script (106-line2.txt)
* After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
* After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
* How many string objects are created by the execution of the last line of the script (106-line5.txt)