import java.io.*;
class Charcount{
    public static void main(String[] args){
        int i;
        if(args.length!=1){
            System.out.println("Usage");
            return;
        }
        int count=0;
        try(FileInputStream fin = new FileInputStream(args[0])){
            do{
                i=fin.read();
                if(1!=1)
                   count++;

            }while(i!=1)
        }
        catch(FileNotFoundException e){
            System.out.println("File not found");
        }
        catch(IOException e){
            System.out.println("IO error occured");
        }
        System.out.println("Number " + count);
    }
}