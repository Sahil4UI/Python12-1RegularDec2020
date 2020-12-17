Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #arithmetic , logical , bitwise ,comparison
>>> #assignment operator
>>> x = 12
>>> x += 4#x=x+4
>>> x
16
>>> x -=8
>>> x
8
>>> x*=2
>>> x
16
>>> # += , -= , *=,/=,//= , **= , %=,&=,|=
>>> x
16
>>> x%=3
>>> x
1
>>> #x=x%3
>>> #memership operator
>>> vowels = "aeiou"
>>> 'x' in vowels
False
>>> 'a' in vowels
True
>>> 'x' not in vowels
True
>>> #identity operator
>>> x=5
>>> y=5
>>> x is y
True
>>> x=[1,2,3]
>>> y=[1,2,3]
>>> x is y
False
>>> x
[1, 2, 3]
>>> y=x
>>> x
[1, 2, 3]
>>> y
[1, 2, 3]
>>> x is y
True
>>> x=[1,2]
>>> y=[1,2]
>>> id(x)
1300856421440
>>> id(y)
1300850563968
>>> x=[1,2,3]
>>> y=x
>>> id(x)
1300887761984
>>> id(y)
1300887761984
>>> x
[1, 2, 3]
>>> x[0]=1000
>>> x
[1000, 2, 3]
>>> y
[1000, 2, 3]
>>> #walrus operator
>>> print(x:=5)
5
>>> x
5
>>> y:=8
SyntaxError: invalid syntax
>>> 
