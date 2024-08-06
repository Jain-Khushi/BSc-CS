import java.awt.*;
import java.awt.event.*;
public class AWTButtons extends Frame implements ActionListener{
    String msg;
    public AWTButtons(){
        setLayout(new FlowLayout());
       
        Button A = new Button("A");
        Button B = new Button("B");
        
        add(A);
        add(B);

        Label lab = new Label("Press a button");
        add(lab);
        
        A.addActionListener(this);
        B.addActionListener(this);
        
        addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent we){
                System.exit(0);
            }
        });
    }
    public void actionPerformed(ActionEvent ae){
        String str = ae.getActionCommand();
        if(str.equals("A")){
            msg = "Name:Khushi Jain | Course:BSc(hons.)Computer Science | Roll Number:204024 | College:SGGSCC";
        }
        else if(str.equals("B")){
            msg = "CGPA in previous semester was 9.18";
        }
        
        repaint();
    }
    public void paint(Graphics g){
        g.drawString(msg,20,100);
    }
    public static void main(String[] args) {
        AWTButtons b = new AWTButtons();
        b.setSize(new Dimension(600,400));
        b.setTitle("Button Demo");
        b.setVisible(true);
    }
}
