Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="helo"
>>> x.isalpha()
True
>>> x="hello12345"
>>> x.isalpha()
False
>>> x.isalnum()
True
>>> x="97789"
>>> x.isdigit()
True
>>> x = "@#"
>>> x.isidentifier()
False
>>> x = "is
SyntaxError: EOL while scanning string literal
>>> x = "is"
>>> x.isidentifier()
True
>>> x = "if"
>>> x.isidentifier()
True
>>> #ASCII - American standard code for information interchange
>>> #ord,chr
>>> ord("A")
65
>>> #ord - ordinal -
>>> ord("@")
64
>>> chr(99)
'c'
>>> #operators:
>>> #arithmetic Operator
>>> # + - / // ** * %
>>> #comparison operator
>>> 12 > 90
False
>>> 12 < 90
True
>>> 12<=12
True
>>> 100>=10
True
>>> 10 == 10#equality operator
True
>>> 10 != 100#not equals
True
>>> #logical operators
>>> #and,or,not
>>> 12 > 13 and 13 > 10 and 90 == 90
False
>>> 102 > 13 and 13 > 10 and 90 == 90
True
>>> #or-atleast one condition must be true
>>> 12 > 13 or 13 > 100 or 90 == 90
True
>>> #not->  true-false , false-true
>>> 10==10
True
>>> not 10==10
False
>>> not 10>100
True
>>> #bitwise operator
>>> # &-bitwise and
>>> 12 & 32
0
>>> 57 & 74
8
>>> 23 & 49
17
>>> # | - bitwise or
>>> 33 & 7
1
>>> 33 | 7
39
>>> #left shift & right shift operators
>>> 27 << 1
54
>>> 27 <<2
108
>>> 
