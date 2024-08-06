import java.util.Scanner;
class Series {
    public static void main(String args[]) {
        Scanner sc= new Scanner(System.in);
        int n,i=1;
        double sum=0.0;
        System.out.println("Enter the n");
        n=sc.nextInt();
        while(i<=n){
            sum = sum + Math.pow(i,i);
            ++i;
        }
        System.out.println("Sum is " + sum);
        sc.close();
        
    }
    
}
