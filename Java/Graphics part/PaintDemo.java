import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
class PaintDemol extends JPanel{
    Random rand;
    PaintDemol(){
        setBorder(
            BorderFactory.createLineBorder(Color.RED, 5));
            rand = new Random();
    }
    protected void paintComponent(Graphics g){
        super.paintComponent(g);
        int x,y,x2,y2;
        int height = getHeight();
        int width = getWidth();
        Insets ins = getInsets();
        for(int i=0; i<10;i++){
            x= rand.nextInt(width-ins.left);
            y= rand.nextInt(height-ins.bottom);
            x2= rand.nextInt(width- ins.left);
            y2= rand.nextInt(height-ins.bottom);
            g.drawLine(x,y,x2,y2);
        }
    }
}
class PaintDemo{
    JLabel jlab;
    PaintDemol pp;
    PaintDemo(){
        JFrame jfrm = new JFrame("Paint Demo");
        jfrm.setSize(200,150);
        jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        pp = new PaintDemol();
        jfrm.add(pp);
        jfrm.setVisible(true);

    }
    public static void main(String[] args){
        
                PaintDemo obj = new PaintDemo();
            }
}