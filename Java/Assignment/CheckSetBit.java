import java.util.Scanner;
class CheckSetBit {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the number : ");
        int num = in.nextInt();

        System.out.print("Enter the bit to be checked : ");
        int n = in.nextInt();

        if ((num & (1 << n)) > 0)
        System.out.println("The bit is set.");
        else
        System.out.println("The bit is not set.");

        in.close();
    }
    
}
