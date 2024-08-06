import javax.swing.*;
//import java.awt.*;
import java.awt.event.*;

public class Counter implements ActionListener {
    JFrame f = new JFrame("Counter");
    int x = 0;
    JTextField tf;

    Counter() {
        
        f.setSize(500, 500);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel l = new JLabel("Counter");
        l.setBounds(20, 10, 80, 30);
        tf = new JTextField(Integer.toString(x));
        tf.setBounds(20, 60, 80, 30);
        tf.setEditable(false);//text field contents cannot be altered by the user
        JButton btn = new JButton("Count");
        btn.setBounds(10, 200, 80, 60);
        btn.addActionListener(this);

        f.add(l);
        f.add(tf);
        f.add(btn);

        f.setLayout(null); //or use this -> f.setLayout(new FlowLayout()); and remove setBounds() method.
        f.setVisible(true);
    }

        public void actionPerformed(ActionEvent ae){
            if(ae.getActionCommand().equals("Count")){
                x++;
                tf.setText(Integer.toString(x));
            }
        }

        public static void main(String[] args) {
            new Counter();
        }
    }
    
