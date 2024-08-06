import java.awt.*;
import java.awt.event.*;



public class KeyEventsM extends Frame implements KeyListener, WindowListener{

	String msg = "Key Listener Demo";
	int X = 50, Y = 100; // output coordinates

	public KeyEventsM() 
	{
		addKeyListener(this); //Register the listener
		addWindowListener(this);
	}

	public void keyPressed(KeyEvent ke) 
	{
		msg = "Key Down";
		repaint();
	}

	public void keyReleased(KeyEvent ke) 
	{
		msg = "Key Up";
		repaint();
	}
	public void keyTyped(KeyEvent ke) 
	{
		msg += ": " + ke.getKeyChar();
		repaint();
	}

	public void windowActivated(WindowEvent we){
		
	}

	public void windowClosed(WindowEvent we){
		
	}

	public void windowDeactivated(WindowEvent we){
		
	}

	public void windowDeiconified(WindowEvent we){
		
	}

	public void windowIconified(WindowEvent we){
		
	}

	public void windowOpened(WindowEvent we){
		
	}

	public void windowClosing(WindowEvent we){
		System.exit(0);
	}

	// Display keystrokes.
	public void paint(Graphics g) 
	{
		g.setColor(Color.black);
		g.drawString(msg, X, Y);
	}

	public static void main(String[] args)
	{
		KeyEventsM obj = new KeyEventsM();

		obj.setSize(new Dimension(300, 300));
		obj.setTitle("Keyboard Events Demo");
		obj.setVisible(true);
	}
}