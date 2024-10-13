import java.util.Scanner;
class IntegerSwap  {
 
    public static void main(String args[])
    {
        Scanner in = new Scanner( System.in );
        System.out.print("Enter the first number : ");
        int x =in.nextInt();
        
        System.out.print("Enter the second number : ");
        int y=in.nextInt();

        System.out.println("Numbers before swapping: x = " + x + ", y = " + y);
 
        x = x ^ y; 
        y = x ^ y; 
        x = x ^ y; 
 
        System.out.println("Numbers after swapping: x = " + x + ", y = " + y);
        in.close();
    }
}