import p1.Shape;
import p2.Rectangle;
import p3.Circle;
public class Areas {
    public static void main(String[] args){
        Rectangle r = new Rectangle(10.0,10.0);
        Circle c = new Circle(5.0);
        Shape s;
        s=r;
        s.area();
        s=c;
        s.area();
    }
}
