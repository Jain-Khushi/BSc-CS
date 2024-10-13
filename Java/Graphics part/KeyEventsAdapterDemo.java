import java.awt.*;
import java.awt.event.*;



public class KeyEventsAdapterDemo extends Frame {

	String msg = "";
	int X = 50, Y = 100; // output coordinates

	public KeyEventsAdapterDemo() 
	{
		addKeyListener(new MyKeyAdapter(this)); //Register the listener
		addWindowListener(new MyWindowAdapter());
	}

	
	// Display keystrokes.
	public void paint(Graphics g) 
	{
		//setBackground(Color.green);  to set background color
		//setForeground(Color.red);   to set font color
		g.setColor(Color.black);
		g.drawString(msg, X, Y);
	}

	public static void main(String[] args)
	{
		KeyEventsAdapterDemo obj = new KeyEventsAdapterDemo();

		obj.setSize(new Dimension(300, 300));
		obj.setTitle("Keyboard Events Demo using Adapter class");
		obj.setVisible(true);
	}
}


class MyKeyAdapter extends KeyAdapter
{
	KeyEventsAdapterDemo obj;

	public MyKeyAdapter(KeyEventsAdapterDemo obj)
	{
		this.obj = obj;
	}

	public void keyPressed(KeyEvent ke) 
	{
		obj.msg = "Key Down";
		obj.repaint();
	}
}


class MyWindowAdapter extends WindowAdapter
{
	public void windowClosing(WindowEvent we){
		System.exit(0);
	}
}
