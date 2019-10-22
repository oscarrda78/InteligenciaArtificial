from matplotlib import pyplot 
from PerceptonSimple import *
import os

def generarDirectorio():
    actualPath=os.getcwd()
    if not "Imagenes" in os.listdir(actualPath):
        os.mkdir(actualPath+"\Imagenes")

pruebas=[Patron(-1,-1,-1),Patron(1,-1,-1),Patron(-1,1,-1),Patron(1,1,1)]
generarDirectorio()
epocas=input("Inserte el numero de Epocas: ")
app=PerceptonSimple(pruebas,int(epocas))
app.testing()

