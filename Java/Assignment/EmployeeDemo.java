class Employee{
    int id,salary;
    String firstName,lastName;

    Employee(int a , String first, String last,int s){
        id=a;
        firstName= first;
        lastName=last;
        salary=s;
    }
    int getID(){
        return id;
    }
    String getFirstName(){
        return firstName;
    }
    String getLastName(){
        return lastName;
    }
    String getName(){
        return firstName +" " + lastName;
    }
    int getsalary(){
        return salary;
    }
    void setsalary(){
        salary= 999;
    }
    int getAnnualSalary(){
        int annual= 12*salary;
        return annual;
    }
    int raiseSalary(){
        int increased= (int)(salary*(0.1));
        int newsalary= salary + increased;
        return newsalary;
    }
    public String toString(){
        return "Employee[id=" + id + ",name =" + firstName + " " + lastName + ",Salary =" + salary + "]";
    }
}
class EmployeeDemo{
    public static void main(String args[]){
        Employee e = new Employee(8, "Peter", "Tan", 2500);
        System.out.println(e);
        e.setsalary();
        System.out.println(e);
        System.out.println("Id is: " + e.getID());
        System.out.println("First Name is: " + e.getFirstName());
        System.out.println("Last Name is: " + e.getLastName());
        System.out.println("Salary is: " + e.getsalary());
        System.out.println("Name is: " + e.getName());
        System.out.println("Annual Salary is: " + e.getAnnualSalary());
        System.out.println(e.raiseSalary());
        System.out.println(e);

    }
}
