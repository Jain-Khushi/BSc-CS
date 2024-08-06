import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class SwingKeyPink{
    public SwingKeyPink(){

        JFrame jfrm = new JFrame("Swing Program");
    jfrm.setLayout(new FlowLayout());
    jfrm.setSize(260,210);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    jfrm.getContentPane().setBackground(Color.pink);
    
    JLabel jl = new JLabel();
    jl.setText("My name is Khushi Jain.");
    jfrm.add(jl);

    jfrm.setVisible(true);
}
    public static void main(String[] args){
        SwingKeyPink obj = new SwingKeyPink();
    }
}

