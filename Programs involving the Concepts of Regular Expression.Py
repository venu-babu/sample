>>> import re
>>> x = 'New year 2017'
>>> re.findall('\d+', x)
['2017']
>>> re.findall('(.*) ', x)
['New year']
