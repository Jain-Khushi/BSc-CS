import java.util.Scanner;

public class exceptionDemo{

	static void test(int a) throws UnderAge{
		if(a<18){
			throw new UnderAge(a);
		}
	}

	public static void main(String[] args){
		int age;
		Scanner sc=new Scanner(System.in);
		System.out.print("Please enter your age for voating: ");
		age=sc.nextInt();
		sc.close();
		try{
			test(age);
		    System.out.println("You are eligible for voating.");
		}
		catch(UnderAge e){
			System.out.println(e);
		}
	}
}

class UnderAge extends Exception{
	private int age;
	UnderAge(int a){
		age=a;
	}

	public String toString(){
		return "UnderAge: "+age;
	}
}
