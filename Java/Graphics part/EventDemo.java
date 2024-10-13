import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
class EventDemo{
    JLabel jlab;
    EventDemo(){
    JFrame jfrm = new JFrame("A simple program");
    jfrm.setLayout(new FlowLayout());
    jfrm.setSize(225,90);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JButton jbtnAlpha = new JButton("Alpha");
    JButton jbtnBeta = new JButton("Beta");

    jbtnAlpha.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent ae){
            jlab.setText("Alpha was pressed");
        }
    });
    jbtnBeta.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent ae){
            jlab.setText("Beta was pressed");
        }
    });
    
    jfrm.add(jbtnAlpha);
    jfrm.add(jbtnBeta);
    jlab = new JLabel("Press a button ");
    jfrm.add(jlab);
    jfrm.setVisible(true);

}
public static void main(String[] args){
    EventDemo obj = new EventDemo();
}
}