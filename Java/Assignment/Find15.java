import java.util.Scanner;
class Find15 {
    static int print(int arr[],int index,int n){
        if(index==n-1)
           return 0;
        if(arr[index]==15)
           return 1 + print(arr,index+1,n);
        else
           return print(arr,index+1,n);
    }

    public static void main(String[] args){
        int index=0,n;
        
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        n=sc.nextInt();
        int arr[]=new int[n];
        System.out.println("Enter the array of integers :");
        for(int i=0;i<n;i++)
        arr[i]=sc.nextInt();
        
        int count=print(arr,index,n);
        System.out.println("The number 15 appears " + count + " times in the array.");
        sc.close();
    }
    
}
