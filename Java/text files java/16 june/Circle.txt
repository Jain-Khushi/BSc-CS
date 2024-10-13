package p3;
import p1.Shape;
public class Circle extends Shape {
    double radius;
    public Circle(){
        radius=0;
    }
    public Circle(double r){
        radius=r;
    }
    public void area(){
        double A=(3.14)*radius*radius;
        System.out.println("Area of Circle : " + A);
    }
    
}
