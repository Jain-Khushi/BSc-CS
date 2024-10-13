import java.util.Scanner;
class DecToHexmine{
    public static void main (String[] args){
        int num=0,rem=0;
        Scanner in=new Scanner(System.in);
        System.out.println("Enter a decimal number: ");
        num=in.nextInt();

        if(num<0)
        {
            System.out.println("The number cannot be negative.");
            return;
        }
        System.out.print("The equivalent hexadecimal number is: ");

        while(num!=0)
        {
            rem=num%16;
            num=num/16;
            if(rem>9)
            {
                switch(rem)
                {
                    case 10: System.out.print("A");
                             break;
                    case 11: System.out.print("B");
                             break;
                    case 12: System.out.print("C");
                             break;
                    case 13: System.out.print("D");
                             break;
                    case 14: System.out.print("E");
                             break;
                    case 15: System.out.print("F");
                             break;
                }
            }
            else
               System.out.print(rem);
        }
        in.close();
    }

}