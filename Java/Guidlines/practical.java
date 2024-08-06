import java.awt.*;
import java.awt.event.*;

public class practical extends Frame {

	String msg = "My name is KHUSHI JAIN";
	int X = 50, Y = 100; // output coordinates

	public practical() 
	{
		
		addWindowListener(new MyWindowAdapter());//Register the listener
	}

	/*public void keyPressed(KeyEvent ke) 
	{

	}

	public void keyReleased(KeyEvent ke) 
	{
		
	}
	public void keyTyped(KeyEvent ke) 
	{
		
	}*/class MyWindowAdapter extends WindowAdapter
{
	public void windowClosing(WindowEvent we){
		System.exit(0);
	}
}

    
	// Display keystrokes.
	public void paint(Graphics g) 
	{
        setBackground(Color.yellow);
		g.setColor(Color.blue);
		g.drawString(msg, X, Y);
	}

	public static void main(String[] args)
	{
		practical obj = new practical();

		obj.setSize(new Dimension(300, 300));
		obj.setTitle("Background color");
		obj.setVisible(true);
	}
}

