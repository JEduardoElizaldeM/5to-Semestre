import simpy
from Nodo import *
from Canales.CanalBroadcast import * ##Mayusculas 


class NodoVecinos(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de conocer a los
        vecinos de tus vecinos.'''

    def __init__ (self,id_nodo,vecinos,canal_entrada,canal_salida):
        self.id_nodo =  id_nodo 
        self.vecinos =  vecinos  # Vecinos del proceso
        self.canal_entrada = canal_entrada 
        self.canal_salida = canal_salida 
        self.identificadores =  set() # {id_nodo} -> esto si es un conjunto, {} ->diccionario 

    def toString(self) :
        return f"Nodo : {self.id_nodo}, vecinos:  {self.vecinos}, identicadores = {self.identificadores}"

    def get_id(self):
        return self.id_nodo
    
    def conoce_vecinos(self,env):
        "Implementacion del algoritmo"
        self.canal_salida.envia(self.vecinos,self.vecinos)

        while True  : # espera a que haya un mensjae en el canal 
            mensaje  =  yield self.canal_entrada.get()  
            self.identificadores.update(mensaje)
            #print(self.toString()) #Mirar proceso de Ejecucion



env = simpy.Environment()
bc_pipe = CanalComuniacion(env)

grafica =  [[1],[0,2,3],[1,4,5],[1],[2],[2]]
sistema_distribuido =  []

#tick = 1

for i in range(0, len(grafica)):
            sistema_distribuido.append(NodoVecino(i, grafica[i],
                                       bc_pipe.crea_canal_entrada(), bc_pipe))

                        
for nodo in sistema_distribuido:
    env.process(nodo.conoce_vecinos(env))


env.run(until=10)

#
print("Grafica : ", grafica )
print("Final de ejecucion")

for nodo in sistema_distribuido :
    print(nodo.toString())

     
