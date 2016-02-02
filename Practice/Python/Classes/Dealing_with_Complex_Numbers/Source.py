class Complex:
    #Classe qui représente un nombre complexe
    #Attributs:
    # - x : partie réelle du nombre complexe (float)
    # - y : partie imaginaire du nombre complexe (float)
    
    #Constructeur
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
        
    #Représentation de la classe en une string (return string)
    def __str__(self):
        if self.y >= 0:
            return "{:1.2f}+{:1.2f}i".format(self.x, abs(self.y))
        else:
            return "{:1.2f}-{:1.2f}i".format(self.x, abs(self.y))
        
    #Ajout de deux complexs
    def __add__(self, toAdd):
        res = complex(self.x,self.y) + complex(toAdd.getX(),toAdd.getY())
        return Complex(float(res.real),float(res.imag))
    
    #Soustraction de deux complexs
    def __sub__(self,toSub):
        res = complex(self.x,self.y) - complex(toSub.getX(),toSub.getY())
        return Complex(float(res.real),float(res.imag))  
    
    #Multiplication de deux complexs
    def __mul__(self,toMult):
        res = complex(self.x,self.y) * complex(toMult.getX(),toMult.getY())
        return Complex(float(res.real),float(res.imag)) 
    
    #Division de deux complexs
    def __truediv__(self,toDiv):
        res = complex(self.x,self.y) / complex(toDiv.getX(),toDiv.getY())
        return Complex(float(res.real),float(res.imag)) 
    
    #Module d'un complex
    def __abs__(self):
        res = abs(complex(self.x,self.y))
        return Complex(float(res),float(0))

a, b = list(map(float,input().split()))
c, d = list(map(float,input().split()))
C1 = Complex(a,b)
C2 = Complex(c,d)

print(C1 + C2)
print(C1 - C2)
print(C1 * C2)
print(C1 / C2)
print(abs(C1))
print(abs(C2))