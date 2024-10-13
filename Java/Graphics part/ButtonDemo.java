import java.awt.*;
import java.awt.event.*;
public class ButtonDemo extends Frame implements ActionListener{
    String msg;
    Button yes,no,maybe;
    public ButtonDemo(){
        setLayout(new FlowLayout());
        yes = new Button("Yes");
        no=  new Button("No");
        maybe = new Button("Undecided");
        add(yes);
        add(no);
        add(maybe);
        yes.addActionListener(this);
        no.addActionListener(this);
        maybe.addActionListener(this);

        addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent we){
                System.exit(0);
            }
        });
    }
    public void actionPerformed(ActionEvent ae){
        String str = ae.getActionCommand();
        if(str.equals("Yes")){
            msg = "You pressed yes";
        }
        else if(str.equals("No")){
            msg = "You pressed no";
        }
        else{
            msg="You pressed undecided";
        }
        repaint();
    }
    public void paint(Graphics g){
        g.drawString(msg,20,100);
    }
    public static void main(String[] args) {
        ButtonDemo appwin = new ButtonDemo();
        appwin.setSize(new Dimension(250,300));
        appwin.setTitle("Button Demo");
        appwin.setVisible(true);
        
    }

}