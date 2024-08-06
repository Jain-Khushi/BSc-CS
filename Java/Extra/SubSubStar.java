

class Star {
    static String s = " ";
    protected Star(){
        s+="Start";
    }
    
}
class SubStar extends Star{
    private SubStar(){
        s+="sub";
    }
} 
public class SubSubStar extends Star{
    private SubSubStar(){
        s+="subsub";
    }
    public static void main(String[] args) {
        new SubSubStar();
        System.out.println(s);
    }

    
}
