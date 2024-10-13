public class Factorial {
    static int fact(int n){
        if(n<=1)
           return 1;
        else 
           return n * fact(n-1);

    }
    public static void main(String args[]){
        int f=fact(3);
        System.out.println("f=" + f);
    }

    
}
