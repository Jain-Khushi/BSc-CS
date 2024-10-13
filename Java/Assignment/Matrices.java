import java.util.Scanner;
class Matrices{
    static int addMatrices(int A[][],int B[][],int n,int C[][]){
        
        for(int i=0;i<n;i++)
           for(int j=0;j<n;j++)
              C[i][j]=A[i][j]+B[i][j];
        
        for(int i=0;i<n;i++){
           for(int j=0;j<n;j++){
             return C[i][j];}
             
        }
        return 0;
}
    public static void main(String args[]){
        int i;
        int j;
        Scanner sc=new Scanner(System.in);

        System.out.println("enter size ");
        int n= sc.nextInt();
        int A[][]=new int [20][20];
        int B[][]= new int [20][20];
        int C[][]=new int [20][20];
        int D[][]=new int [20][20];
        
        System.out.println("Enter A");
        for( i=0;i<n;i++)
        for( j=0;j<n;j++)
            A[i][j]= sc.nextInt();

            System.out.println("Enter B");
        for( i=0;i<n;i++)
        for( j=0;j<n;j++)
            B[i][j]= sc.nextInt();
            
            for( i=0;i<n;i++)
            for( j=0;j<n;j++)
        D[i][j]=addMatrices(A,B,n,C);
        System.out.println("Matrices c is");
        for( i=0;i<n;i++){
          for( j=0;j<n;j++){
             System.out.print(C[i][j] + " "); 
          }
          System.out.println();
        }           
            sc.close();

    }
}