>>> with open('venu.txt', 'w') as f:
...     f.write('venuk')
...     f.close()
... 
>>> with open('venu.txt', 'r') as f:
...     rows = f.readlines()
...     print rows
