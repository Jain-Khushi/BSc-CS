import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
class practicalCount implements ActionListener{
    int x=0;
    JFrame jfrm = new JFrame("A program");
    JTextField jtf = new JTextField(15);
    practicalCount(){
    
    jfrm.setLayout(new FlowLayout());
    jfrm.setSize(700,300);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    JButton jbtn = new JButton("Count");
    JLabel jlab = new JLabel("Counter");
    jfrm.add(jlab);

    jbtn.addActionListener(this);
    
    jfrm.add(jtf);
    jfrm.add(jbtn);
    jfrm.setVisible(true);

}
public void actionPerformed(ActionEvent ae){
    if(ae.getActionCommand().equals("Count")){
        x++;
        jtf.setText(Integer.toString(x));
    }
}
public static void main(String[] args){
    practicalCount obj = new practicalCount();
}
}

