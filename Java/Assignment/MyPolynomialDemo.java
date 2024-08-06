import java.util.Scanner;

//class to create a polynomial
class MyPolynomial {

    // instance variable
    private double[] coeffs;

    // parameterised constructor
    MyPolynomial(double[] coeffs) {
        this.coeffs = coeffs;
    }

    
    int getDegree() {
        return coeffs.length - 1;
    }

    
    public String toString() {
        String equation = "" + coeffs[0];
        for (int i = 1; i < coeffs.length; i++) {
            if (i == 1) {
                equation = coeffs[i] + "x + " + equation;
            } else {
                equation = coeffs[i] + "x^" + i + " + " + equation;
            }
        }
        return equation;
    }

    
    double evaluate(double x) {
        double result = coeffs[0];
        for (int i = 1; i < coeffs.length; i++) {
            result = result + coeffs[i] * Math.pow(x, i);
        }
        return result;
    }

    MyPolynomial add(MyPolynomial another) {
        int bigger;
        int smaller;
        if (coeffs.length > another.coeffs.length) {
            bigger = coeffs.length;
            smaller = another.coeffs.length;
        } else {
            bigger = another.coeffs.length;
            smaller = coeffs.length;
        }
        MyPolynomial temp = new MyPolynomial(new double[bigger]);
        int i;
        for (i = 0; i < smaller; i++) {
            temp.coeffs[i] = coeffs[i] + another.coeffs[i];
        }
        while (i < coeffs.length) {
            temp.coeffs[i] = coeffs[i];
            i++;
        }
        while (i < another.coeffs.length) {
            temp.coeffs[i] = another.coeffs[i];
            i++;
        }
        return temp;
    }

}

// driver class
public class MyPolynomialDemo {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the degree of the Polynomial: ");
        int degree = sc.nextInt();

        double[] coefficients = new double[degree + 1];

        System.out.println("Enter the coefficients of the First Polynomial seperated by spaces.");
        for (int i = degree; i >= 0; i--) {
            coefficients[i] = sc.nextDouble();
        }

        MyPolynomial p1 = new MyPolynomial(coefficients);

        System.out.println("Degree of the polynomial: " + p1.getDegree());
        System.out.println("First polynomial: " + p1);

        System.out.print("Enter the value of x: ");
        double x = sc.nextDouble();

        System.out.println("Evaluation of polynomial: " + p1.evaluate(x));

        System.out.print("Enter the degree of the Second Polynomial: ");
        degree = sc.nextInt();

        coefficients = new double[degree + 1];

        System.out.println("Enter the coefficients of the Second Polynomial seperated by spaces.");
        for (int i = degree; i >= 0; i--) {
            coefficients[i] = sc.nextDouble();
        }

        sc.close();

        MyPolynomial p2 = new MyPolynomial(coefficients);
        System.out.println("Second polynomial: " + p2);

        MyPolynomial p3 = p1.add(p2);
        System.out.println("Addition of these two polynomials: " + p3);
    }

}
