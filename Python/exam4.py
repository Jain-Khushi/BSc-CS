def Model(Dict1:dict,model):
    k= Dict1.get(model)
    if(k!=None):
        return k
    else:
        return -1
def Change(Dict1:dict,VM):
    k=Dict1.get(VM)
    if(k!=None and k<5):
        Dict1.pop(VM)
    elif(k!=None and k>5):
        Dict1[VM]=k-2

#part1
Dict1={'BMW':5,'Mercedes':10,'Volkswagen':10,'Jaguar':4,'Landrover':15}
print("Number of vehicles available : ",Model(Dict1,'BMW'))

#part2
Change(Dict1,'Volkswagen')
print("Updated dictionary : ",Dict1)

#part3
def swap(T1:tuple,T2:tuple):
    T2,T1=Tuple1,Tuple2
    return T1,T2

Tuple1=(11,22,33)
Tuple2=(99,88,77)
Tuple1,Tuple2=swap(Tuple1,Tuple2)
print("Tuple1 : ",Tuple1)
print("Tuple2 : ",Tuple2)

#part4
def Div3and5(t1:tuple):
    sum3=0
    sum5=0
    sum3and5=0
    for i in range(len(t1)):
        if(t1[i]%3==0):
            sum3=sum3+t1[i]
        elif(t1[i]%5==0):
            sum5=sum5+t1[i]
        elif(t1[i]%3==0 and t1[i]%5==0):
            sum3and5=sum3and5+t1[i]
    return sum3,sum5,sum3and5
Tsum=(1,2,3,4,5,6,7,8,9,10)
s3,s5,s3and5 = Div3and5(Tsum)
print("Sum of elements divisible by 3 : ",s3)
print("Sum of elements divisible by 5 : ",s5)
print("Sum of elements divisible by 3 and 5 : ",s3and5)

#part5
set1={10,20,30,40,50}
set2={30,40,50,60,70}
print("Common elements : ",set1.intersection(set2))

#part6
set3=set1.difference(set2)
set4=set2.difference(set1)
print("Elements : ",set3.union(set4))
