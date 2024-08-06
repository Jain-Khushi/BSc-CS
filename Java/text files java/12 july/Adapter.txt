import java.awt.*;
import java.awt.event.*;

public class Adapter extends Frame {

	String msg = "Keyboard Event Demo using Adapter class";
	int X = 100, Y = 100; // output coordinates

	public Adapter() 
	{
		addKeyListener(new MyKeyAdapter(this)); //Register the listener
        addWindowListener(new MyWindowAdapter());
	}

	// Display keystrokes.
	public void paint(Graphics g) 
	{
		setBackground(Color.pink); 
		setForeground(Color.black);  
		g.drawString(msg, X, Y);
	}

	public static void main(String[] args)
	{
		Adapter obj = new Adapter();

		obj.setSize(new Dimension(500, 500));
		obj.setTitle("Adapter Demo");
		obj.setVisible(true);
	}
}


class MyKeyAdapter extends KeyAdapter
{
	Adapter obj;

	public MyKeyAdapter(Adapter obj)
	{
		this.obj = obj;
	}

    public void keyTyped(KeyEvent ke) 
	{
		obj.msg = "Typed character is: " + ke.getKeyChar();
		obj.repaint();
	}
}

class MyWindowAdapter extends WindowAdapter
{
	public void windowClosing(WindowEvent we){
		System.exit(0);
	}
}



