print('Выберите желаемую операцию: + - / *')
op=input()
print('Введите числа')
a=int(input())
b=int(input())
if op=='+':
    print(a + b)
if op=='-':
    print(a - b)
if op=='*':
    print(a*b)
if op=='/':
    print(a/b)