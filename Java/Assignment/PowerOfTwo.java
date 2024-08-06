import java.util.Scanner;
class PowerOfTwo {
    public static void main(String args[]){
        Scanner in=new Scanner(System.in);
        System.out.print("Enter the number : ");
        int num = in.nextInt();

        if(num==0)
          {
              System.out.println("Number cannot be zero.");
              return;
          }
        
        int diff = num-1;

        if((num & diff) ==0)
           System.out.println("The number is the power of 2.");
        else
           System.out.println("The number is not the power of 2.");

        in.close();
    }
    
}
