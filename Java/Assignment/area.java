class shape {
    void show(){
        System.out.println("Superclass show");
    }
    
}
class rectangle extends shape{
    void show(){
        System.out.println("Subclass rectangle show");
    }
}
class triangle extends shape{
    void show(){
        System.out.println("Subclasss triangle show");
    }
}
public class area {
    public static void main(String[] args) {
        rectangle r =new rectangle();
        triangle t = new triangle();
        shape s= new shape();
        s.show();
        s=r;
        s.show();
        s=t;
        s.show();

        
    }
}
