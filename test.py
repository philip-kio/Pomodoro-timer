# x = '00:00'
# def timer(x):
#     x = '00:00'
#     m,s=map(int,x.split(':'))
#     if s < 59:
#         s += 1
#     elif s==59:
#         s = 0
#         if m <25:
#             m += 1
#         elif m == 25:
#             m= 00
#             s= 00
#             if m < 10:
#                 m= 0 + str(m)
#             else:
#                 m= str(m)
#             if s < 10:
#                 s= str(s)
#             else:
#                 s= str(s)
#         return m
#
#
# print(timer(x))
import time

y= '00:00'
x,s = map(int, y.split(':'))
while s <59:
    time.sleep(1)
    s += 1
    print (s)
    if s == 59:
        s=00
        x +=1
        print (f'{x} minutes')
    if x == 1:
        print ('Pondoro time for work is up!')

        break


print(f'{x}:{s}')