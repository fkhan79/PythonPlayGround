#fibonacci
def f(n):
    sumup=0
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
        print(a)
        if a%2==0:
            sumup +=a
    return sumup

val=input("Enter the range:")
print("Sum of Even Valued term till %s is %i" %(val,f(int(val))))