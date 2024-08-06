import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class SwingCharacter{
    String key = " ";
    public SwingCharacter(){

        JFrame jfrm = new JFrame("Swing Program");
        jfrm.setLayout(new FlowLayout());
        jfrm.setSize(260,210);
        jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    
        JLabel jl1 = new JLabel("Typed character is: ");
        JLabel jl2 = new JLabel(" ");
        jfrm.add(jl1);
        jfrm.add(jl2);

        jfrm.addKeyListener(new KeyAdapter(){
            public void keyTyped(KeyEvent k){
                String str = ""+k.getKeyChar()+"";
                jl2.setText(str);
            }
        });

        jfrm.setVisible(true);
    }
    public static void main(String[] args){
        SwingCharacter obj = new SwingCharacter();
    }
}
