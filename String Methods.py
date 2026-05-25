Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string methods
>>> #len()
>>> a="python"
>>> len(a)
6
>>> b="python course"
>>> len(b)
13
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> 
>>> #count()
>>> a="twinkle twinkle little star"
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkle")
2
>>> a.count("little")
1
a.count("i")
3
a.count(" ")
3
a.count("")
28
a.count(t)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.count(t)
NameError: name 't' is not defined

#find a string
a="python"
a.find("h")
3
a.find("python")
0
a.find(T)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.find(T)
NameError: name 'T' is not defined
a.find("P")
-1
a.find("")
0

#escape sequences
#\n -> new line
#\t -> tab space
a="name\nmobileno\tmailid"
print(a)
name
mobileno	mailid
b="name:Dinesh\tmobileno:8247523259\tmailid:dinesh@gmail.com"
print(b)
name:Dinesh	mobileno:8247523259	mailid:dinesh@gmail.com
b="name:Dinesh\nmobileno:8247523259\nmailid:dinesh@gmail.com"
print(b)
name:Dinesh
mobileno:8247523259
mailid:dinesh@gmail.com
b="name:Dinesh\t\t\tmailid:dinesh@gmail.com"
print(b)
name:Dinesh			mailid:dinesh@gmail.com


#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a.replace("wait","work",1)
'work until you succeed'
b="wait wait until you succeed"
b.repalce("wait,"work")
          
SyntaxError: unterminated string literal (detected at line 1)
b.replace("wait","work")
          
'work work until you succeed'
a
          
'wait until you succeed'
b
          
'wait wait until you succeed'


#strip()
          
#lstrip(),rstrip()
          
a="       pooja      "
          
a.strip()
          
'pooja'
a.lstrip()
          
'pooja      '
a.rstrip()
          
'       pooja'
