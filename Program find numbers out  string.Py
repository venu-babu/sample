>>> x='venu1993babu' [Any value assign to x]
>>> xx = []
>>> for i in x:
...     if i.isdigit():
...         xx.append(i)
... 
>>> xx
['1', '9', '9', '3']
>>> ''.join(xx)
'1993'
