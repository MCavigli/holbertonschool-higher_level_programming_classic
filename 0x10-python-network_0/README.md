# 0x10. Python - Network #0

## Resources
* [HTTP (HyperText Transfer Protocol)](https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/http_basics.html)(except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
* [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
* [Using cURL to debug](https://intranet.hbtn.io/concepts/51)

## Requirements
* All your scripts should be exactly 3 lines long (wc -l file should print 3)
* All your files should end with a new line
* The first line of all your bash files should be exactly #!/bin/bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* All your files must be executable
* All curl commands must be have the option -s (silent mode)

## TASKS

### TASK 0
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

* The size must be displayed in bytes
* You have to use curl
Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
```

File: `0-body_size.sh`

### TASK 1
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

* Display only body of a 200 status code response
* You have to use curl
Please test your script in the container provided, using the web server running on port 5000

```

guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$
```

File: `1-body.sh`

### TASK 2
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

* You have to use curl
Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$
```

File: `2-delete.sh`

### TASK 3
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

* You have to use curl
Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 
```

File: `3-methods.sh`

### TASK 4
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

* A header variable X-HolbertonSchool-User-Id must be sent with the value 98
* You have to use curl
Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
guillaume@ubuntu:~/0x10$ 
```

File: `4-header.sh`

### TASK 5
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

* A variable email must be sent with the value hr@holbertonschool.com
* A variable subject must be sent with the value I will always be here for PLD
* You have to use curl
Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: hr@holbertonschool.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 
```

File: `5-post_params.sh`

### TASK 6
Technical interview preparation:

* You are not allowed to google anything
* Whiteboard first
Write a function that finds a peak in a list of unsorted integers.

* Prototype: def find_peak(list_of_integers):
* You are not allowed to import any module
* Your algorithm must have the lowest complexity
* 6-peak.py must contain the function
* 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)

```
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 
```

File: `6-peak.py, 6-peak.txt`