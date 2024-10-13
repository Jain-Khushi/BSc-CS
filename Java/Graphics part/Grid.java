import java.awt.*;
import java.awt.event.*;
public class Grid extends Frame{
    static final int n=4;
    public Grid(){
        setLayout(new GridLayout(n,n));
        setFont(new Font("SansSerif" , Font.BOLD,24));
        for(int i = 0;i<n;i++){
            for(int j=0 ; j<n ; j++){
                int k = i*n+j;
                if(k>0)
                  add(new Button("" + k));
            }
        }
        addWindowListener(new WindowAdapter(){
            public void WindowClosing(WindowEvent e)
            {
                System.exit(0);
            }
        });

    }
    public static void main(String[] args)
{
    Grid obj = new Grid();

    obj.setSize(new Dimension(370,700));
    obj.setTitle(" Grid Layout ");
    obj.setVisible(true);
}
}