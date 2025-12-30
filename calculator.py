a=int(input('Enter first Number:'))
b=int(input('Enter second Number'))
c=input('Enter operation to be done (+,-,*,/,//,%,**):')
if c == '+':
    print(a,'+',b,'is:',(a+b))
elif c == '-':
    print(a,'-',b,'is:',(a-b))
elif c == '*':
    print(a,'*',b,'is:',(a*b))
elif c == '/':
    print(a,'/',b,'is:',(a/b))
elif c == '//':
    print(a,'//',b,'is:',(a//b))
elif c == '%':
    print(a,'%',b,'is:',(a%b))
elif c == '**':
    print(a,'**',b,'is:',(a**b))
else:
    print("Invalid operator")