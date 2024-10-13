class TwoDim {
    int x;
    int y;
    
    TwoDim(){
        x=0;
        y=0;
    }
    TwoDim(int a,int b){
        x=a;
        y=b;
    }
    void print(){
        System.out.print("x= " + x + " y= " + y);
    }
}
class ThreeDim extends TwoDim {
    int z;
    ThreeDim(){
        super();
        z=0;
    }
    ThreeDim(int a,int b,int c){
        super(a,b);
        z=c;
    }
    void print(){
        super.print();
        System.out.println(" z= " + z);
    }
}
public class dimension {
    public static void main(String[] args) {
        TwoDim obj = new ThreeDim(1,2,3);
        obj.print();
    }
}

