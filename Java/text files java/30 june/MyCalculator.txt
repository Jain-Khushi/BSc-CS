import java.util.Scanner;
public class MyCalculator implements AdvancedArithmetic {
    
    public int divisorSum(int n){
        int sum=0;
        for(int i=1; i<=n; i++ ){
            if(n % i == 0)
            sum = sum +  i;
        }
        return sum;
    }
    public static void main(String args[]){
        int n,s;
        Scanner sc =  new Scanner (System.in);
        MyCalculator M = new MyCalculator();

        System.out.println("Enter the number (should not more than 1000) : " );
        n = sc.nextInt();
        s = M.divisorSum(n);
        System.out.println("The sum of divisors is : " + s);

        sc.close();
    }
}
