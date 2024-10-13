import math

print("(a)")
#9 x 10
#invalid syntax because to multiply 2 numbers we use asterisk(*) symbol,correction:
print(9 * 10)

print("(b)")
#1 1/2 + 2 2/3
#invalid syntax because multiplication symbol(*) is missing,correction:
print(1*1/2 + 2*2/3)

print("(c)")
#3cos(35)
#invalid syntax because to multiply we need to add asterisk sign and to apply cos function we need to do math.cos,correction:
print(3*math.cos(35))

print("(d)")
#8.31x10^9
#invalid syntax because to multiply 2 numbers we use asterisk(*) symbol and to perform power operation we can add power function or can do exponentiation,correction:
print(8.31*math.pow(10,9))    #or
print(8.31*(10**9))

print("(e)")
#7%+8%+9%
#invalid syntax because we cannot use percentage sign in calculation,correction:
print(7/100+8/100+9/100)

print("(f)")
#(-)54.2+9.2
#invalid syntax because negative sign is used without brackets,correction:
print(-54.2+9.2)

print("(g)")
#'5'/'4'
#stings cannot be divided,correction:
print(5/4)

print("(h)")
#ln(e)-math.log(10)
#there is no function as ln() in python math module,correction:
print(math.log(math.e)-math.log(10))
