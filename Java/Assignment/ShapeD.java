class TwoDshape{
    private double radius;
    TwoDshape(double r){
        radius=r;
    }
    double Getr(){
        return radius;
    }
    void setr(double r){
        radius=r;
    }
    void show(){
        System.out.println("Radius: " + radius);
    }
}
class Circle extends TwoDshape{
   
    Circle(double r){
        super(r);
    }
    void area(){
        double A=(3.14)*Getr()*Getr();
        System.out.println("AREA is " + A);
    }
}
public class ShapeD{
    public static void main(String args[]) {
        Circle C= new Circle(7);
        C.area();
        
    }
}