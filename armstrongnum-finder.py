def anum(a,b,c): #function for armstrong number
    LHS = (a*100) + (b*10) + c
    RHS = (a**3)+ (b**3) + (c**3)
    if LHS == RHS:
        print(f"Combination Matches {LHS} = {RHS}\nYour required digits are {a},{b},{c}\n")
lis = [num for num in range(1000)] #I just made one linier code which contain number 0 to 999
for i in range(10):
    anum(0, 0, i)
for j in range(10, 101):
    num_str = str(lis[j])
    a = 0
    b = int(num_str[0])
    c = int(num_str[1])
    anum(a, b, c)
for k in range(100, 1000):
    num_str = str(lis[k])
    a = int(num_str[0])
    b = int(num_str[1])
    c = int(num_str[2])
    anum(a, b, c)
