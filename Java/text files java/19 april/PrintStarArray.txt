import java.util.Scanner;
class PrintStarArray 
{
    public static void main(String[] args)
    {
        int num=0;
        Scanner in=new Scanner(System.in);
        System.out.print("Enter the number of items :");
        num=in.nextInt();

        if(num<0)
        {
            System.out.println("\nThe number of items cannot be negative.");
            return;
        }

        int items[]=new int[num];
        System.out.print("Enter the values of all items(non-negative integer and separated by space):");
        for(int i=0; i<items.length; i++)
            items[i]=in.nextInt();

        for(int i=0; i<items.length; i++)
        {
            System.out.print(i + ": ");
            for(int j=0; j<items[i]; j++)
                System.out.print("*");
            System.out.println("(" + items[i] + ")");
         }

         in.close();
     }

}
    

