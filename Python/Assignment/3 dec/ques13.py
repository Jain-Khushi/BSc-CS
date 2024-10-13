import matplotlib.pyplot as plt
import math


def sineCurve():
    plt.subplot(2, 1, 1)
    degrees = range(0, 360 + 1)
    sineValues = [math.sin(math.radians(i)) for i in degrees]
    plt.plot(sineValues)
    plt.xlabel("Degree")
    plt.ylabel("Sine Values")
    plt.title("Sine Curve")
    plt.grid()


def cosineCurve():
    plt.subplot(2, 1, 2)
    degrees = range(0, 360 + 1)
    cosineValues = [math.cos(math.radians(i)) for i in degrees]
    plt.plot(cosineValues)
    plt.xlabel("Degree")
    plt.ylabel("Cosine Values")
    plt.title("Cosine Curve")
    plt.grid()


sineCurve()
cosineCurve()
plt.tight_layout()
plt.show()

# import matplotlib.pyplot as plt
def polynomialCurve(a, b, step):
    nsteps = int((b - a) / step)
    x = [a + step * i for i in range(nsteps + 1)]
    y1 = [t ** 2 for t in x]
    y2 = [t ** 3 for t in x]
    plt.plot(x, y1, "ro--", label="X vs X**2")
    plt.plot(x, y2, "b<-.", label="X vs X**3")
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("X vs X*2 and X vs X*3")
    plt.grid()


a = float(input("Enter first element of the range : "))
b = float(input("Enter the last element of the range : "))
step = float(input("Enter step size : "))
polynomialCurve(a, b, step)
plt.tight_layout()
plt.show()
# Enter first element of the range : 1
# Enter the last element of the range : 10
# Enter step size : 2

# import matplotlib.pyplot as plt
def exponentialCurve():
    plt.subplot(2, 1, 1)
    degrees = range(0, 360 + 1)
    expvalues = [math.exp(math.radians(i)) for i in degrees]
    plt.plot(expvalues)
    plt.xlabel("DEGREE")
    plt.ylabel("EXPONENTIAL VALUES")
    plt.title("EXPONENTIAL CURVE")
    plt.grid()
    plt.show()


exponentialCurve()
