package p2;
import p1.Shape;
public class Rectangle extends Shape {
    double length,breadth;
    public Rectangle(){
        length=0;
        breadth=0;
    }
    public Rectangle(double a ,double b){
        length=a;
        breadth=b;
    }
    public void area(){
        double A=length * breadth;
        System.out.println("Area of Rectangle : " + A);
    }
}
