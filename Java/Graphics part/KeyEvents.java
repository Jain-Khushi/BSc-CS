import java.awt.*;
import java.awt.event.*;

//KeyEvents is both the source and listener for our events
public class KeyEvents extends Frame implements KeyListener,WindowListener{

    String msg = "Key Listener Demo";
    int X = 50, Y = 100; //coordinates of key

    //Register listeners in constructor
    public KeyEvents(){
        //These two methods are a part of Component class whose subclass is Frame
        addKeyListener(this);
        addWindowListener(this);
    }

    public void keyPressed(KeyEvent ke){
        msg = "Key Down";
        repaint();
    }

    public void keyReleased(KeyEvent ke){
        msg = "Key Up";
        repaint();
    }

    public void keyTyped(KeyEvent ke){
        msg += ": " + ke.getKeyChar();
        repaint();
    }
    public void windowActivated(WindowEvent we){
		
    }
    
    public void windowClosed(WindowEvent we){
        
    }
    
    public void windowDeactivated(WindowEvent we){
        
    }
    
    public void windowDeiconified(WindowEvent we){
        
    }
    
    public void windowIconified(WindowEvent we){
        
    }
    
    public void windowOpened(WindowEvent we){
        
    }
    
    public void windowClosing(WindowEvent we){
        System.exit(0);
    }
    
    
    
    //Display keystrokes
    public void paint(Graphics g){
        g.setColor(Color.black); //Used to set the font color 
        g.drawString(msg,X,Y); //Used to display a msg at coordinates X and Y
    }

    public static void main(String args[]){
        KeyEvents obj = new KeyEvents();

        obj.setSize(new Dimension(300, 300));
        obj.setTitle("Key Events Demo");
        obj.setVisible(true);
    }
}
