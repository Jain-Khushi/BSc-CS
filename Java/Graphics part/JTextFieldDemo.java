import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class JTextFieldDemo{
    public JTextFieldDemo(){

        JFrame jfrm = new JFrame("A simple program");
    jfrm.setLayout(new FlowLayout());
    jfrm.setSize(260,210);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    JTextField jtf = new JTextField(15);
    jfrm.add(jtf);
    JLabel jl = new JLabel();
    jfrm.add(jl);

    jtf.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent ae){
            jl.setText(jtf.getText());
        }
    });
    jfrm.setVisible(true);
}
    public static void main(String[] args){
        JTextFieldDemo jj = new JTextFieldDemo();
    }
}
