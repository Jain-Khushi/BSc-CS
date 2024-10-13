import java.util.Scanner;
class Numbers{
    int x;
    int y;
    Numbers()
    {
         x=0;
         y=0;
    }
    Numbers(int a,int b)
    {
         x=a;
         y=b;
    }
    
    void add(Numbers n1,Numbers n2){
        int real=n1.x + n2.x;
        int imaginary=n1.y + n2.y;
        System.out.println(real + "+ i" + imaginary);
    }
    void multiply(Numbers n1,Numbers n2){
        int real=n1.x*n2.x - n1.y*n2.y;
        int imaginary=n1.x*n2.y + n1.y*n2.x;
        System.out.println(real + "+ i" + imaginary);
    }
    public String toString() 
	{
 		return x + " + i " + y;
 	}

}
class Complex{
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the real part of first complex number");
        int x1 = in.nextInt();
        System.out.println("Enter the imaginary part of first complex number");
        int y1 = in.nextInt();
        System.out.println("Enter the real part of second complex number");
        int x2 = in.nextInt();
        System.out.println("Enter the real part of second complex number");
        int y2 = in.nextInt();

        Numbers c= new Numbers();
        Numbers c1= new Numbers(x1,y1);
        Numbers c2= new Numbers(x2,y2);

        System.out.println("Complex number 1:" + c1);
        System.out.println("Complex number 2:" + c2);

        c.add(c1,c2);
        c.multiply(c1,c2);

        in.close();
    }
}

