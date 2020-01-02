year = int(input('Input year:'))
is_leap_year = False
if year % 100 == 0:
    if year % 400 ==0:
        is_leap_year = True
elif year % 4 == 0:
    is_leap_year = True
else:
    is_leap_year = False
print('是闰年' if(is_leap_year) else '不是闰年')