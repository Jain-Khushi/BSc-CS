import javax.swing.*;
class SwingDemo{
    SwingDemo(){
    JFrame jfrm = new JFrame("A simple program");
    jfrm.setSize(275,100);
    jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JLabel jlab = new JLabel("Swing ");
    jfrm.add(jlab);
    jfrm.setVisible(true);

}
public static void main(String[] args){
    SwingDemo obj = new SwingDemo();
}
}