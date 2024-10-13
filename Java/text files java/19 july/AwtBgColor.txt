import java.awt.*;
import java.awt.event.*;
public class AwtBgColor extends Frame{
    
    public AwtBgColor(){
        setLayout(new FlowLayout());
        
        Button Red = new Button("Red");
        Button Blue =new Button("Blue");
        add(Red);
        add(Blue);

        Label lab = new Label("Press a color");
        add(lab);

        addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent we){
                System.exit(0);
            }
        });

    Red.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent ae){
            setBackground(Color.red);
        }
    });

    Blue.addActionListener(new ActionListener(){
        public void actionPerformed(ActionEvent ae){
            setBackground(Color.blue);
        }
    });

    
}
    public static void main(String[] args) {
        AwtBgColor b = new AwtBgColor();
        b.setSize(new Dimension(250,300));
        b.setTitle("Background Demo");
        b.setVisible(true);
    }
}