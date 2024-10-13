import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class SwingMouseEvents{

    String msg = "";

    public SwingMouseEvents(){
        JFrame jfrm = new JFrame("Mouse Events Demo");
        jfrm.setLayout(new FlowLayout());
        jfrm.setSize(new Dimension(300,300));
        jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel jlab = new JLabel(" ");
        jlab.setText("Mouse Events");
        jfrm.add(jlab);
        
    
    jfrm.addMouseListener(new MouseAdapter(){
        public void mouseClicked(MouseEvent m){
           
            jfrm.setSize(new Dimension(300, 300)); //frame will reduce to its original size
            msg = "Mouse clicked.Frame reduced to its original size.";
            jlab.setText(msg);
        }
    });

    jfrm.addMouseListener(new MouseAdapter(){
        public void mouseEntered(MouseEvent m){
            
            jfrm.setSize(new Dimension(900, 900));  //size of the frame will be tripled
            msg = "Mouse entered.Size of the frame will be tripled.";
            jlab.setText(msg);
        }
    });

    jfrm.addMouseListener(new MouseAdapter(){
        public void mouseExited(MouseEvent m){
            System.exit(0);
        }
    });
    jfrm.setVisible(true);
    }

    public static void main(String args[]){
        SwingMouseEvents obj = new SwingMouseEvents();
    }
}
