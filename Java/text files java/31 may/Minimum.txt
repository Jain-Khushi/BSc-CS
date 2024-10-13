import java.util.Scanner;
class Minimum {
    static int driver(int arr[],int index,int len){
        int min;
        
        if(index==len-1)
           return arr[index];
        else{
            min=driver(arr,index + 1,len);
            if(arr[index] < min)
              min = arr[index];
            return min;  
        }  
    }
    public static void main(String args[]){
        int index=0,m;
        Scanner sc=new Scanner(System.in);

        System.out.println("Enter the size of array :");
        int len= sc.nextInt();

        int arr[]=new int[len];
        System.out.println("Enter the array of integers :");
        for(int i = 0; i< len; i++)
        arr[i]=sc.nextInt();

        m=driver(arr,index,len);
        System.out.println("The minimum element in the array is " + m);
        sc.close();
    }    
}
