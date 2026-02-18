a = int(input("Enter 1st nummber: "))
b = int(input("Enter 2nd nummber: "))
c = int(input("Enter 3rd nummber: "))

out = "True" if (a+b>c and a+c>b and b+c>a) else "False"
input(out)
