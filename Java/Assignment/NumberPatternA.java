import java.util.Scanner;
class NumberPatternA {
    public static void main (String args[]) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the size : ");
        int size = in.nextInt();

        for(int i=0 ; i<size ; i++)
        {
            int num=1;
            for(int j=0 ; j<=i ; j++)
            {
                System.out.print(num + " ");
                ++num;
            }
            System.out.print("\n");
        }
        in.close();
    }
}