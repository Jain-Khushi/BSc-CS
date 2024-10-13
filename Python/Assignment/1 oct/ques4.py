s1=[2,3,4,5,6]
print("Input :",s1)
s2=[2*i if i%2==0 else -abs(i)for i in s1]
print("Output :",s2)
