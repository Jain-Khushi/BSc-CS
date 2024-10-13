import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
class SwingButtons{
    JLabel jlab;
    SwingButtons(){
    JFrame jfrm = new JFrame("A simple program");
    jfrm.setLayout(new FlowLayout());
    jfrm.setSize(700,300);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JButton jbtnA = new JButton("A");
    JButton jbtnB = new JButton("B");

    jbtnA.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent ae){
            jlab.setText("Name:Khushi Jain | Course:BSc(hons.)Computer Science | Roll Number:204024 | College:SGGSCC");
        }
    });
    jbtnB.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent ae){
            jlab.setText("CGPA in previous semester was 9.18");
        }
    });
    
    jfrm.add(jbtnA);
    jfrm.add(jbtnB);
    jlab = new JLabel("Press a button ");
    jfrm.add(jlab);
    jfrm.setVisible(true);

}
public static void main(String[] args){
    SwingButtons obj = new SwingButtons();
}
}
