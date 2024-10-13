
class Student:
  def __init__(self, name,):
    self.name = name
    self.avg = 0
    print(f"Name: {name}")
    
  def __del__(self):
    print("Destructor called, object deleted.")

  def sub(self, m1,m2,m3):
    self.m1= m1
    self.m2= m2
    self.m3= m3
    print(f"Marks of subject 1  : {m1}",f"\nMarks of subject 2  : {m2}",f"\nMarks of subject 3  : {m3}")
    
  
name=input("Enter your name: ")
m1=int(input("Enter marks of subject 1: "))
m2=int(input("Enter marks of subject 2: "))
m3=int(input("Enter marks of subject 3: "))
st1=Student(name)
st1.sub(m1,m2,m3)
st1.avg=(m1+ m2+ m3)//3
print(f"Average of marks: {st1.avg}")
del st1
