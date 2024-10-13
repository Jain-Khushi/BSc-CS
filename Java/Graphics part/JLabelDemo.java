import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class JLabelDemo{
    public JLabelDemo(){
        JFrame jfrm = new JFrame("A simple program");
    jfrm.setLayout(new FlowLayout());
    jfrm.setSize(260,210);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    ImageIcon ii = new ImageIcon("Pictures");
    JLabel jl = new JLabel("Hourglass", ii, JLabel.CENTER);
    jfrm.add(ii);
    jfrm.setVisible(true);

    public static void main(String[] args){
        JLabelDemo jj = new JLabelDemo();
    }
    }
}