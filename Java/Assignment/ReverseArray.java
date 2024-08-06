import java.util.Scanner;
class ReverseArray {
    static void Reverse(int index,int arr[]){
        if(index==arr.length)
          return;
        else{
            Reverse(index+1,arr);
            System.out.print(arr[index] + " ");
        }
    }
    public static void main(String args[]) {
        int index=0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size");
        int n=sc.nextInt();

        int arr[]=new int [n];

        System.out.println("Enter the aray");
        for(int i=0;i<n;i++)
        arr[i]=sc.nextInt();
        
        System.out.println("The reversed array is : ");
        Reverse(index,arr);
        
    }
    
}
