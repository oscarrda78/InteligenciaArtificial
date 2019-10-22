import random
from matplotlib import pyplot 



class Punto2D():
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Patron():
    def __init__(self,x1,x2,valorEsperado):
        
        self.x1=x1
        self.x2=x2
        self.valorEsperado=valorEsperado
class PerceptonSimple():
    def __init__(self,pruebas,epocas):
        self.__W1=1
        self.__W2=1
        self.__Wumbral=0.5
        self.__pruebas=pruebas
        self.__epocas=epocas
    def __getFuncionActivacion(self,patron):
        return -1 if (self.__W1*patron.x1+self.__W2*patron.x2+self.__Wumbral<=0) else 1
    def __calibrarPesos(self,patron):
        self.__W1=self.__W1+patron.valorEsperado*patron.x1
        self.__W2=self.__W2+patron.valorEsperado*patron.x2
        self.__Wumbral=self.__Wumbral+patron.valorEsperado
    def __getSegundaEntrada(self,patron):
        return -((self.__W1/self.__W2)*patron.x1)-(self.__Wumbral/self.__W2)
    def __getPrimeraEntrada(self,patron):
        return -(patron.x2*(self.__W2/self.__W1))-(self.__Wumbral/self.__W1)
    def __getPuntosRecta(self,patron):
        primerPunto=Punto2D(self.__pruebas[0].x1,self.__getSegundaEntrada(self.__pruebas[0]))
        segundoPunto=Punto2D(self.__getPrimeraEntrada(self.__pruebas[0]),self.__pruebas[0].x2)
        return dict(punto1=primerPunto,punto2=segundoPunto)
    
    def __graficarEntradas(self):
        for patron in self.__pruebas:
            if patron.valorEsperado==-1:
                pyplot.plot(patron.x1,patron.x2,marker='o', markersize=5, color="red")
            else:
                pyplot.plot(patron.x1,patron.x2,marker='o', markersize=5, color="green")
            
    def __graficar(self,punto1,punto2,epoca):
        pyplot.plot([punto1.x,punto2.x],[punto1.y,punto2.y],marker='o', markersize=1, color="blue")
        self.__graficarEntradas()
        pyplot.axhline(0,color="black")
        pyplot.axvline(0,color="black")
        pyplot.xlim(-5,5)
        pyplot.ylim(-5,5)
        pyplot.title("Epoca {}".format(epoca))
        pyplot.savefig("Imagenes\Epoca{}.png".format(epoca))
        pyplot.show()
    def graficarEpoca(self,epoca,patron=None):
        if patron!=None:
            patron=self.__pruebas[0]
        prueba=self.__getPuntosRecta(patron)
        self.__graficar(prueba["punto1"],prueba["punto2"],epoca)


    def testing(self):
        self.graficarEpoca(0)
        print("Epoca {}".format(0))
        print("W1: {}, W2: {}, Wumbral: {}".format(self.__W1,self.__W2,self.__Wumbral))
        for epoca in range(1,self.__epocas+1):
            print("Epoca {}".format(epoca))
            for patron in self.__pruebas:
                valorFuncionActivacion=self.__getFuncionActivacion(patron)
                while  valorFuncionActivacion!=patron.valorEsperado:
                    self.__calibrarPesos(patron)
                    valorFuncionActivacion=self.__getFuncionActivacion(patron)
                print("W1: {}, W2: {}, Wumbral: {}".format(self.__W1,self.__W2,self.__Wumbral))
        
            self.graficarEpoca(epoca,self.__pruebas[-1])


        
if __name__ == '__main__':
    pass
    
