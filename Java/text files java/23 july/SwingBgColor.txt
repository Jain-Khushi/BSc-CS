import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
class SwingBgColor{
    JLabel jlab;
    SwingBgColor(){
    JFrame jfrm = new JFrame("A button program");
    jfrm.setLayout(new FlowLayout());
    jfrm.setSize(225,150);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JButton jbtnRed = new JButton("Red");
    JButton jbtnBlue = new JButton("Blue");
    
    jbtnRed.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent ae){
            jfrm.getContentPane().setBackground(Color.red);
        }
    });
    jbtnBlue.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent ae){
            jfrm.getContentPane().setBackground(Color.blue);
        }
    });
    
    jfrm.add(jbtnRed);
    jfrm.add(jbtnBlue);
    jlab = new JLabel("Press a color ");
    jfrm.add(jlab);
    jfrm.setVisible(true);

}
public static void main(String[] args){
    SwingBgColor obj = new SwingBgColor();
}
}