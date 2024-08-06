import java.util.Scanner;
class NumberPatternB {
    public static void main (String args[]) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the size : ");
        int size = in.nextInt();

        for (int i = 1; i <= size; i++) {
            for (int j = 1; j <= size; j++) {
                System.out.print(( j >= i ? (j-i+1) : " ") + " ");
            }
            System.out.println();
        }
        in.close();
    }
}