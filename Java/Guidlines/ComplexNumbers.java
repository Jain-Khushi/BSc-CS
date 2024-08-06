
import java.util.Scanner;

class Complex
{
 	int x;
 	int y;

	Complex(int real, int imaginary) 
	{
 		this.x = real;
 		this.y = imaginary;
 	}


	Complex add(Complex obj) 	
	{
 		return new Complex(
 		this.x + obj.x,
 		this.y + obj.y
 		);
 	}

	Complex multiply(Complex obj) 
	{
 		return new Complex(
 		this.x * obj.x - this.y * obj.y,
 		this.x * obj.y + obj.x * this.y
		);
 	}

	public String toString() 
	{
 		return x + " + i " + y;
 	}
}

class ComplexNumbers
{
 	public static void main(String[] args) 
	{
		int x1 , x2 , y1, y2;

		Scanner in = new Scanner(System.in);

		System.out.print ("Enter the real and imaginary part of first complex no. : ");              

		x1=in.nextInt();

		y1=in.nextInt();

		System.out.print ("Enter the real and imaginary part of second complex no. : ");              

		x2=in.nextInt();

		y2=in.nextInt();

 		Complex c1 = new Complex(x1, y1);

 		Complex c2 = new Complex(x2, y2);

 		System.out.println("Complex 1: " + c1);

 		System.out.println("Complex 2: " + c2);

 		System.out.println("Sum: " + c1.add(c2));

 		System.out.println("Product: " + c1.multiply(c2));

		in.close();
 	}
}