class X{
    int a;
    X(int i){
        a=i;
    }
}
class Y extends X{
    int b;
    y(int i,int j){
        b=i;
    }
}
class M {
    public static void main (String args[]) {
        X xob1 = new X[10];
        X xob2;
        Y yob = new Y(5,6);
        xob2 = xob1;
        System.out.println("xob2.a = " + xob2.a);
        xob2=yob;
        System.out.println("xob2.a = " + xob2.a);
        xob2.a=21;
        xob2.b=32;
        
    }
    
}
