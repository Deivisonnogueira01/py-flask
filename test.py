<<<<<<< HEAD
a = '1+2-3*4/5.5#'

c = a.translate({42:'', 43:'', 45:'', 46:'', 47:''})
print(c)
if c.isdecimal(): print('OK1')
if c.isnumeric(): print('OK2')
if c.isdigit(): print('OK3')
=======
from random import random

print(random() * 0xffffff)
print(round(random() * 0xffffff))
print(f'{123:06X}')
print(f'#{round(random() * 0xffffff):06X}')


>>>>>>> 2d5b0afe34fed9fcae6cfb7dd2aa30e6af51cbb1

