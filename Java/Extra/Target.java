import java.util.Scanner;
public class Target {
    static boolean search(int nums[],int pos,int target){
        if(pos == nums.length)
            return false;
        else if(nums[pos] == target)
            return true;
        else return search(nums,pos+1,target);
    }
    public static void main(String[] args){
        int arr[]=new int[20];
        int tar,i,n;
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
