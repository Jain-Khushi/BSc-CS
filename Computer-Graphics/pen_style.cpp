#include <iostream.h>
#include <graphics.h>
#include <conio.h>  
#include <stdlib.h>
#include <stdio.h>
#include <graphics.h>  
#include <dos.h>  

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "c:\\turboc3\\bgi");

    int x1, y1, x2, y2, choice;

    cout << "Enter the starting point (x1, y1): ";
    cin >> x1 >> y1;

    cout << "Enter the ending point (x2, y2): ";
    cin >> x2 >> y2;

    cout << "Choose a line style: " << endl;
    cout << "1. Dashed Line" << endl;
    cout << "2. Dotted Line" << endl;
    cout << "3. Dashed & Dotted Line" << endl;

    cin >> choice;


    switch (choice) {
        case 1: // Dashed Line
            setlinestyle(DASHED_LINE, 0, 1);
            break;
        case 2: // Dotted Line
            setlinestyle(DOTTED_LINE, 0, 1);
            break;
        case 3: // Dashed & Dotted Line
            setlinestyle(DASHED_LINE, 0, 1);
            break;
        default:
            cout << "Invalid choice" << endl;
            closegraph();
            return 0;
    }

    if (choice == 3) { // Dashed & Dotted Line
        line(x1, y1, x2, y2);
        setlinestyle(DOTTED_LINE, 0, 1);
        line(x1, y1, x2, y2);
    } else { // Dashed Line or Dotted Line
        line(x1, y1, x2, y2);
    }

    getch();
    clrscr();
    closegraph();
    return 0;
}
