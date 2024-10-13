import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class JToggleButtonDemo{
    public JToggleButtonDemo(){
        JFrame jfrm = new JFrame("A simple program");
    jfrm.setLayout(new FlowLayout());
    jfrm.setSize(260,210);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    JLabel jlab = new JLabel("Button is off");
    JToggleButton jtbn= new JToggleButton("on/off");
    jtbn.addItemListener(new ItemListener(){
        public void itemStateChanged(ItemEvent ie){
            if(jtbn.isSelected())
               jlab.setText("button is on");
            else 
               jlab.setText("button is on");
        }
    });
    jfrm.add(jtbn);
    jfrm.add(jlab);
    jfrm.setVisible(true);
}
public static void main(String[] args){
    JToggleButtonDemo obj = new JToggleButtonDemo();
}
}