class Top{
    public Top(String s){
        System.out.println("B");
    }
}
public class Bottom extends Top {
    public Bottom(String s){
        System.out.println("D");
    }
    public static void main(String[] args){
        new Bottom("C");
        System.out.println(" ");
    }
    
}
