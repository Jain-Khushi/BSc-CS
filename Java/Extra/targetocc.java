import java.util.Scanner;
public class targetocc {
    static int count =0;
    static int search(int nums[],int pos,int target){
        
        if(pos > nums.length-1)
            return count;
         if(nums[pos]==target) 
         count++;
        return search(nums,pos+1,target);
    }
    public static void main(String[] args){
        int arr[]=new int[20];
        int tar,i,n,occ=0;
        //boolean b;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements");
        n = sc.nextInt();
        System.out.println("Enter the array");
        for(i=0;i<n;i++)
        arr[i]=sc.nextInt();

        System.out.println("Enter the target element");
        tar = sc.nextInt();
        //b=search(nums,i,tar);
        System.out.println(search(arr,0,tar));
        sc.close();
    }
    
}

