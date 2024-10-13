import java.util.Scanner;
class Pattern {
    public static void main(String args[]) {
        Scanner sc= new Scanner(System.in);
        int n;
        System.out.println("enter n");
        n=sc.nextInt();
        int A[][]=new int [20][20];
        System.out.println("The pattern is ");

        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(i==j || i>j)
                System.out.print(i + " ");
            }
            System.out.println();
        }
        sc.close();
    }
    
}
