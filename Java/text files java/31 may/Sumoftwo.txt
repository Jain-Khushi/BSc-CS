import java.util.Scanner;
class Sumoftwo {
    static int add(int a,int b){
        if(b==0)
          return a;
        else
           return 1 + add(a,b-1);
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number :");
        int a = sc.nextInt();
        System.out.println("Enter the second number :");
        int b = sc.nextInt();
        
        int s=add(a,b);
        System.out.println("The sum is : " + s);

        sc.close();

    }
}
