n = int(raw_input("Enter number "))
p = 2
while p <= n:
    is_prime=True
    for i in range(2, p):
        if p%i == 0:
            is_prime=False
            break;
    if is_prime==True:
        print "%d is a Prime Number\n" % p
    p=p+1
