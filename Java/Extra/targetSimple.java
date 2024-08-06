import java.util.Scanner;
public class targetSimple {
    
    public static void main(String[] args){
        int arr[]=new int[20];
        int tar,i,n,flag=0,pos=0;
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements");
        n = sc.nextInt();

        System.out.println("Enter the array");
        for(i=0;i<n;i++)
        arr[i]=sc.nextInt();

        System.out.println("Enter the target element");
        tar = sc.nextInt();

        for(i=0;i<n;i++){
            if(arr[i]==tar){
              flag=1;
              pos=i;
            }
        }
        if(flag==1)
            System.out.println("Element found at " + (pos+1));   
        else
            System.out.println("Element not found"); 
        
        sc.close();
    }    
}

