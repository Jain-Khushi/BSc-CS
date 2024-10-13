import java.util.Scanner;
class PensionContributionCalculator{
    public static void main(String[] args){

    
       int salary=0, age=0;    
       double employeeContribution=0.0, employerContribution=0.0, totalContribution=0.0;

       Scanner in=new Scanner(System.in);
       System.out.print("Enter the monthly salary: ");
       salary=in.nextInt();
       System.out.print("Enter the age: ");
       age=in.nextInt();
    
       if (age <= 55)
       {
           employeeContribution=salary*0.2;
           employerContribution=salary*0.17;
       }        
       else if (age <= 60)
       {
           employeeContribution=salary*0.13;
           employerContribution=salary*0.13; 

       }
       else if (age <= 65)
       {
           employeeContribution=salary*0.075;
           employerContribution=salary*0.09;
       }
       else if(age>65)
       {
           employeeContribution=salary*0.05;
           employerContribution=salary*0.075;
       }
       totalContribution = employeeContribution + employerContribution;

       System.out.println("The employee's contribution is: " + employeeContribution);
       System.out.println("The employer's contribution is: " + employerContribution);
       System.out.println("The total contribution is: " + totalContribution);

       in.close();
    }
}
        