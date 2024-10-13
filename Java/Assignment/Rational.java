import java.util.Scanner;
class Rational {
    static void add(int n1,int d1,int n2,int d2){
        int r1,r2;
        if(d1==d2){
            r1=n1+n2;
            r2=d1;
        }
        else{
            r1=(n1*d2)+(n2*d1);
            r2=d1*d2;
        }
        System.out.println("Sum of rational number is: "+  r1 + "/" + r2  );
    }

    static void multiply(int n1,int d1,int n2,int d2){
        int r3,r4;
        r3=n1*n2;
        r4=d1*d2;
        System.out.println("Product of rational numbers is " + r3 + "/" + r4);
    }

    public static void main(String args[]) {
        Scanner sc= new Scanner(System.in);
       int n1,d1,n2,d2;
       System.out.println("Enter the num of first");
       n1= sc.nextInt();
       System.out.println("Enter the denom of first");
       d1= sc.nextInt();

       System.out.println("Enter the num of second");
       n2= sc.nextInt();
       System.out.println("Enter the denom of second");
       d2= sc.nextInt();

       System.out.println("First rational number: " + n1 + "/" + d1);
       System.out.println("Second rational number: " + n2 + "/" + d2);

       add(n1,d1,n2,d2);
       multiply(n1,d1,n2,d2);

       sc.close();
    
        
    }
    
}
