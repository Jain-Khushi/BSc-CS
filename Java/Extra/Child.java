class Parent{
    private final void methA(){
        System.out.println("parent");

    }
}
public class Child extends Parent{
    public final void methA(){
        System.out.println("child");
    }
    public static void main(String [] args){
        new Child.methA();
    }
}