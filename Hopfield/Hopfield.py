import numpy as np

patron1=""
patron2=""
identity=""
def funcion_activacion_escalon(x):
    return 1 if(x>0) else -1

def inicializar_patrones(*argv):
    global patron1,patron2,identity
    patron1=np.array([argv[0]])
    patron2=np.array([argv[1]])
    identity=np.identity(4,dtype=int)


def matriz_pesos():
    W1=np.subtract(np.dot(patron1.transpose(),patron1),identity)
    W2=np.subtract(np.dot(patron2.transpose(),patron2),identity)
    matriz_sum=np.add(W1,W2)
    return matriz_sum

        
def obtener_patron_similar(prueba):
    matriz_prueba=np.array([prueba])
    salida_prueba=np.dot(matriz_prueba,matriz_pesos())
    result=map(funcion_activacion_escalon,salida_prueba.tolist()[0])
    return list(result)

def main():
    inicializar_patrones([1,1,-1,-1],[-1,-1,1,1])
    pruebas=[[1,-1,-1,-1],[1,1,-1,-1]]
    resultados=[]
    for prueba in pruebas:
        resultados.append(obtener_patron_similar(prueba))
    print(*resultados)
if __name__ == "__main__":
    main()





