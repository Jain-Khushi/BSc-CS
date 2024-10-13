package Guidlines;
import java.io.*;  
public class Line  
{  
    public static void main(String args[])  
    {  
        try  
        {  
            File file=new File("try.txt");    
            FileReader fr=new FileReader(file);   
            BufferedReader br=new BufferedReader(fr);    
            StringBuffer sb=new StringBuffer();      
            String line;  
            System.out.println("Lines that have the first two characters as '//' : ");
            while((line=br.readLine())!=null)  
            {  
                sb.append(line);        
                sb.append("\n"); 
                if(line.charAt(0) =='/'&&line.charAt(1) =='/')
                {
                   System.out.println(line);  
                }
 
            }  
            fr.close();   
        }  
        catch(IOException e)  
        {  
            e.printStackTrace();  
        }  
   }  
}  