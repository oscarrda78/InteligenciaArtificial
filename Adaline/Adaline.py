import random 
import numpy as np
W1=random.random()
W2=random.random()
W3=random.random()
factorAprendizaje=0.3
data=np.array([
    [0,0,1,1],
    [0,1,0,2],
    [0,1,1,3],
    [1,0,0,4],
    [1,0,1,5],
    [1,1,0,6],
    [1,1,1,7]


])



class Adalaine():
    def __init__(self):
        self._w=[round(random.random(),2) for _ in range(3)]
        self._alfa=0.3
        self._cost=[]
    def predict(self,inputs):
        salida=sum(w*elm for w,elm in zip(self._w,inputs))
        return salida
    def updatePesos(self,inputs,error):
        self._w=[w+self._alfa*error*x for w,x in zip(self._w,inputs)]
    def train(self,data):
        bad=False
        iterador=0
        while not bad:
            ErrorCuaMedio=0.0
            for x in data:
                s=self.predict(x[0:-1])
                if x[-1]!=s:
                    iterError=x[-1]-s
                    self.updatePesos=(x[0:-1],iterError)
                    ErrorCuaMedio+=(iterError**2)
            ErrorCuaMedio=ErrorCuaMedio/2.0
            self._cost.append(ErrorCuaMedio)
            iterador+=1
            if ErrorCuaMedio ==0 or iterador>=100:
                print("Numero de iteraciones: {}".format(iterador))
                bad=True

print("Datos")
print(data)
print("entrenando")
ada=Adalaine()
ada.train(data)
print("pesos: ",ada._w)
print("prediccion para entrada ",data[4:-1])
