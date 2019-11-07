import numpy as np

entradas=""
factor_aprendizaje=0.6
pesos=np.array([[0.2,0.8],[0.6,0.4],[0.5,0.7],[0.9,0.3]])

def actualizar_pesos_ganador(ganador):
    global pesos
    for i in range(len(pesos)):
        for j in range(len(pesos[0])):
            if j==ganador:
                pesos[i][j]=pesos[i][j]+factor_aprendizaje*(entradas[i][j]-pesos[i][j])
    







def generar_entradas(patron):
    global entradas
    nuevo=np.array([patron,patron])
    entradas=nuevo.T




generar_entradas([1,1,0,0])


print("Pesos Iniciales")
print(pesos)



def main(iteraciones,*patrones):
    for iteracion in range(iteraciones):
        print("Numero de iteracion {}".format(iteracion+1))
        for i,actual in enumerate(patrones):
            generar_entradas(actual)
            resultante=np.subtract(entradas,pesos)
            resultante_elevado=np.power(resultante,2)
            d_1=resultante_elevado[:,0]
            d_2=resultante_elevado[:,1]
            ganador= 1 if np.sum(d_1) > np.sum(d_2) else 0
            actualizar_pesos_ganador(ganador)
            print("\nResultado del vector {}".format(i+1))
            print(pesos)
            print("Cluster : {}".format(ganador+1))
        
        
main(100,[1,1,0,0],[0,0,0,1],[1,0,0,0],[0,0,1,1])



    
    
    
    
               


