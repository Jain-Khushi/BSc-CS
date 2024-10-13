class Person {

    private String name;

    public Person() {
        name = "No name yet.";
    }

    public Person(String n) {
        name = n;
    }

    public void setName(String newName) {
        name = newName;
    }

    public String getName() {
        return name;
    }

    public void print() {
        System.out.println("Name: " + name);
    }

    public boolean equals(Object p) {
        final Person temp = (Person) p;
        return name.equals(temp.name);
    }
}

class Employee extends Person {

    private double salary;
    private int yearOfJoin;
    private String natInsuranceNum;

    Employee() {
        super();
        salary = 0.0;
        yearOfJoin = 0;
        natInsuranceNum = null;
    }

    Employee(String n, double salary, int yearOfJoin, String natInsuranceNum) {
        super(n);
        this.salary = salary;
        this.yearOfJoin = yearOfJoin;
        this.natInsuranceNum = natInsuranceNum;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public void setYear(int yearOfJoin) {
        this.yearOfJoin = yearOfJoin;
    }

    public void setInsuranceNum(String natInsuranceNum) {
        this.natInsuranceNum = natInsuranceNum;
    }

    public double getSalary() {
        return salary;
    }

    public int getYear() {
        return yearOfJoin;
    }

    public String getInsuranceNum() {
        return natInsuranceNum;
    }

    public boolean equals(Object e) {
        Employee obj = (Employee) e;
        if (getName().equals(obj.getName()) && salary == obj.salary && yearOfJoin == obj.yearOfJoin && natInsuranceNum.equals(obj.natInsuranceNum)) {
            return true;
        } else
            return false;
    }

}

public class EmployeeDriver {

    public static void main(String[] args) {
        Employee e1=new Employee("Daniel",40000,2002,"ABCD");
        Employee e2=new Employee("Peter",30000,2004,"EFGH");
        System.out.println("\nDetails of Employee 1.\n");
        e1.print();
        System.out.println("Salary: " + e1.getSalary());
        System.out.println("Year Of Joining: " + e1.getYear());
        System.out.println("National Insurance Number: " + e1.getInsuranceNum());

        System.out.println("\nDetails of Employee 2.\n");
        e2.print();
        System.out.println("Salary: " + e2.getSalary());
        System.out.println("Year Of Joining: " + e2.getYear());
        System.out.println("National Insurance Number: " + e2.getInsuranceNum());

System.out.println("Are the two employees same?");
System.out.println(e1.equals(e2));

    }
}