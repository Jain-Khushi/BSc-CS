import java.awt.event.*;
import java.awt.*;

public class GraphicsDemo extends Frame
{
    public GraphicsDemo()
    {
        addWindowListener(new WindowAdapter(){
            public void WindowClosing(WindowEvent e)
            {
                System.exit(0);
            }
        }
        );
}
public void paint(Graphics g){
    g.setColor(Color.red);
    g.drawLine(20,40,100,90);
    g.drawLine(20,90,100,40);

    g.drawRect(20,50,60,50);
    g.fillRect(110,150,60,50);

    g.drawRoundRect(200,150,60,50,15,15);
    g.fillRoundRect(290,150,60,50,30,40);

    g.drawOval(20,250,50,50);
    g.drawOval(200,260,100,40);
    g.fillOval(100,250,75,50);

    g.drawArc(20,350,70,70,0,180);
    g.fillArc(70,30,70,70,0,75);

    int xpoints[]={20,200,20,200,20};
    int ypoints[]={450,450,650,650,450};
    int num = 5;

    g.fillPolygon(xpoints,ypoints,num); //xcoordinates,y coordinates,number of sides 
}
public static void main(String[] args)
{
    GraphicsDemo obj = new GraphicsDemo();

    obj.setSize(new Dimension(370,700));
    obj.setTitle(" Graphics Demo ");
    obj.setVisible(true);
}
}