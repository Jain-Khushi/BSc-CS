import java.awt.*;
import java.awt.event.*;

//MouseEvents is both the source and listener for our events
public class MouseEvents extends Frame implements MouseListener,MouseMotionListener{

    String msg = "Hello";
    int mouseX = 50, mouseY = 50; //coordinates of mouse

    //Register listeners in constructor
    public MouseEvents(){
        //These two methods are a part of Component class whose subclass is Frame
        addMouseListener(this);
        addMouseMotionListener(this);
    }

    //Handle mouse clicked.
    public void mouseClicked(MouseEvent me){
        //save coordinates
        mouseX = 50;
        mouseY = 100;
        msg = "Mouse clicked.";
        repaint();
    }

    //Handle mouse entered.
     public void mouseEntered(MouseEvent me) {
        // save coordinates
            mouseX = 50;
            mouseY = 100;
            msg = "Mouse entered.";
            repaint();
        }
        
    // Handle mouse exited.
    public void mouseExited(MouseEvent me) {
        // save coordinates
            mouseX = 50;
            mouseY = 100;
            msg = "Mouse exited.";
            repaint();
        }

    //Handle button pressed.   
    public void mousePressed(MouseEvent me) {
        // save coordinates
            mouseX = 50;
            mouseY = 100;
            msg = "Down";
            repaint();
        }
    
    // Handle button released.
    public void mouseReleased(MouseEvent me) {
        // save coordinates
            mouseX = me.getX();
            mouseY = me.getY();
            msg = "Up";
            repaint();
        }

    public void mouseDragged(MouseEvent me) {
    // save coordinates
        mouseX = me.getX();
        mouseY = me.getY();
        msg = "Dragging mouse at " + mouseX + ", " + mouseY;
        repaint();
    }
        
    // Handle mouse moved.
    public void mouseMoved(MouseEvent me) {
        
        msg = "Moving mouse at " + me.getX() + ", " + me.getY();
        repaint();
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