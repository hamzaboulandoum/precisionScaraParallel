import sympy as sym
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
L = 120
l = 180
D = 230
dθ = 0.005
x_values = []
y_values = []
accuracy = []
def derivativeRespectToθ1(function) :
    return sym.diff(function, θ1)
def derivativeRespectToθ2(function) :
    return sym.diff(function, θ2)


θ1, θ2 = sym.symbols("θ1 θ2")

hSquare = (- L * sym.cos(θ1) + D + L * sym.cos(θ2) )**2 + (L * sym.sin(θ2) - L * sym.sin(θ1) )**2
h = sym.sqrt(hSquare)
cosTheta = (D + L* sym.cos(θ2) - L * sym.cos(θ1)) / h
sinTheta = L *( sym.sin(θ2) - sym.sin(θ1)) / h
HSquare = l**2 - h**2 / 4
H = sym.sqrt(HSquare)
X = L * sym.cos(θ1) + h/2 * cosTheta - H * sinTheta
Y = L * sym.sin(θ1) + h/2 * sinTheta + H * cosTheta

XderivativeRespectToθ1 = derivativeRespectToθ1(X)
YderivativeRespectToθ1 = derivativeRespectToθ1(Y)
XderivativeRespectToθ2 = derivativeRespectToθ2(X)
YderivativeRespectToθ2 = derivativeRespectToθ2(Y)
XDifferential = XderivativeRespectToθ1 * dθ + XderivativeRespectToθ2 * dθ
YDifferential = YderivativeRespectToθ1 * dθ + YderivativeRespectToθ2 * dθ


for o1 in np.linspace(0, np.pi, 360):
    for o2 in np.linspace(0, np.pi, 180):
        HSquareNumber = HSquare.subs(θ1, o1).subs(θ2, o2)
        if HSquareNumber > 0 :
            errorFunction = sym.sqrt(XDifferential**2 + YDifferential ** 2)
            errorNumber = errorFunction.subs(θ1, o1).subs(θ2, o2)
            if errorNumber < 2 :
                if( o1 >= 30*np.pi/180 - np.pi/360  and o1 < 30*np.pi/180 + np.pi/360 and o2 >= 127.49*np.pi/180 - np.pi/360  and o2 < 127.49*np.pi/180 + np.pi/360 ) :
                    print(errorNumber)
                accuracy.append(errorNumber)
                x_values.append(X.subs(θ1, o1).subs(θ2, o2))
                y_values.append(Y.subs(θ1, o1).subs(θ2, o2))
plt.scatter(x_values, y_values, c=accuracy, cmap='turbo', edgecolor='none', s=5)
plt.xlabel("abscisse en mm")
plt.ylabel("ordonnée en mm")
plt.title("La précision d'un robot Scara Parallèle ")
colorbar = plt.colorbar()
colorbar.set_label('Précision moyenne  en millimètre', labelpad=1, y=0.5, rotation=90)
plt.show()