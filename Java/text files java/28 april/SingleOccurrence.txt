import java.util.Scanner;
class SingleOccurrence {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int num=0;

        System.out.print("Enter the number of elements in the array : ");
        num = in.nextInt();

        int array[]=new int[num];

        System.out.println("Enter the elements of the array : ");
        for(int i=0 ; i<array.length ; i++)
           array[i]=in.nextInt();

        int result = array[0];

        for(int i=1 ; i<array.length ; i++)
           result = result^array[i];

        System.out.println("Element occuring once is : " + result);
        
        in.close();
    }
    
}
