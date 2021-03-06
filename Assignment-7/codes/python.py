# B.ASLI
# CS21BTECH11011
# PROBABILITY

# given equation is 10k^2 + 9k - 1 = 0 finding positive roots


from math import sqrt

a = 10
b = 9
c = (-1)

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    d = (float((-b) + sqrt(r))/(2*a))
    e = (float((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (d, e))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()

if (d >= 0) and (d <= 1) :
    print("this is case 1 ")
    print("the value of k is ", d)
    k = "{:.2f}".format(3*d)
    print("the value of p(X < 3) is ", k)
    print("the value of p(X > 3) is ", (7*d*d + d))
    print("the value of p(0 < X < 3) is ", k)

if (e >= 0) and (e <= 1) :
    print("this is case 2 ")
    print("the value of k is ", d)
    k = "{:.2f}".format(3*d)
    print("the value of p(X < 3) is ", k)
    print("the value of p(X > 3) is ", (7*d*d + d))
    print("the value of p(0 < X < 3) is ", k)
    
