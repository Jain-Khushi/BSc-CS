import java.util.Scanner;
class Palindrome
	{
	    public static boolean isPal(String s)
	    {
	        if(s.length() == 0 || s.length() == 1)
	            return true; 
	        if(s.charAt(0) == s.charAt(s.length()-1))
	        return isPal(s.substring(1, s.length()-1));
	        return false;
	    }
	
	    public static void main(String[]args)
	    {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the string : ");
            String str = sc.nextLine();
	        
	        if(isPal(str))
	            System.out.println(str + " is a palindrome");
	        else
	            System.out.println(str + " is not a palindrome");
            
            sc.close();
	    }
	}