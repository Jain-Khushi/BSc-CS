import java.util.Scanner;
class Position{
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n,max=0,pos=0;
        int A[]=new int [20];
        System.out.println("Enter size of elementts ");
        n=sc.nextInt();
        System.out.println("enter elements ");
        for(int i=0;i<n;i++)
        A[i]=sc.nextInt();

        for(int i=0;i<n;i++){
            if(A[i]>max){
              max=A[i];
              pos=i+1;
            }
        }
        System.out.println("the position is " + pos);
        sc.close();
        
    }
}