import java.util.Scanner;
public class starPattern{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of lines");
        int lines=sc.nextInt();

        for(int i=0;i<=lines-1;i++){
          for(int j=0;j<=i;j++){
             System.out.print("*" + " ");}
             System.out.println(" ");
          }
        for(int i=lines-1;i>=0;i--){
            for(int j=0;j<=i-1;j++){
                System.out.print("*" + " ");}
                System.out.println(" ");
        }
        sc.close();
    }
}
