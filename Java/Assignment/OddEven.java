import java.util.Scanner;
class OddEven {
    public static void main(String args[]){
        Scanner in=new Scanner(System.in);
        System.out.print("Enter the number : ");
        int num= in.nextInt();

        int n;

        if((num & 1)== 0)
           System.out.println("The number is even.");
        else
           System.out.println("The number is odd.");

        in.close();
    }
    
}
