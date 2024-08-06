import java.awt.*;
import java.awt.event.*;

//Mouse is both the source and listener for our events
public class MouseEvents extends Frame implements MouseListener{

    String msg = "Key Events Demo";
    int mouseX = 50, mouseY = 50; //coordinates of mouse

    //Register listeners in constructor
    public MouseEvents(){
        //These two methods are a part of Component class whose subclass is Frame
        addMouseListener(this);
    
    }

    //Handle mouse clicked.
    public void mouseClicked(MouseEvent me){
        //save coordinates
        mouseX = 50;
        mouseY = 100;
        setSize(new Dimension(300, 300)); //frame will reduce to its original size
        msg = "Mouse clicked.Frame reduced to its original size.";
        repaint();
    }

    //Handle mouse entered.
     public void mouseEntered(MouseEvent me) {
        // save coordinates
            mouseX = 50;
            mouseY = 100;
            setSize(new Dimension(900, 900));  //size of the frame will be tripled
            msg = "Mouse entered.Size of the will be tripled.";
            repaint();
        }
        
    // Handle mouse exited.
    public void mouseExited(MouseEvent me) {
            System.exit(0);
            repaint();
        }

    public void mouseReleased(MouseEvent me){

    }

    public void mousePressed(MouseEvent me){

    }

    //Display msg at current X,Y location.
    public void paint(Graphics g){
        g.setColor(Color.black); //Used to set the font color 
        g.drawString(msg,mouseX,mouseY); //Used to display a msg at coordinates mouseX and mouseY
    }

    public static void main(String args[]){
        MouseEvents obj = new MouseEvents();

        obj.setSize(new Dimension(300, 300));
        obj.setTitle("Mouse Events Demo");
        obj.setVisible(true);
    }
}
