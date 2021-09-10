import numpy as np   ##Relacion de orden
class Lista:
    __items=None
    __tope=0
    __cant=0
    def __init__(self,xcant):
        self.__items= np.empty(xcant,dtype=int)
        self.__tope=0
        self.__cant= xcant
    def vacia(self):
        return self.__tope == 0
    def llena(self):
        return self.__tope == self.__cant
    def insertar(self,elemento):
        if self.__tope == 0:
            self.__items[self.__tope]= elemento
            self.__tope += 1
        else:
            i=0
            while (elemento > self.__items[i])and(i <= self.__tope):
                i+=1
            for j in range(self.__tope, i, -1):
                self.__items[j]= self.__items[j-1]
            self.__items[i]= elemento
            self.__tope += 1
    def suprimir(self,elemento):
        if self.__tope == 0:
            print("ERROR, Lista Vacia")
        else:
            i=0
            while(elemento != self.__items[i])and(i<self.__tope):
                i+=1
            if i == self.__tope:
                print("El elemento no se encuetra en la lista")
            else:
                aux=self.__items[i]
                for j in range(i,self.__tope,+1):
                    self.__items[j]=self.__items[j+1]
                self.__tope -= 1
                return aux
    def recorrer(self):
        for i in range(self.__tope):
            print(self.__items[i])
    def primerElemento(self):
        if self.vacia() == False:
            return self.__items[0]
        else:
            print("La Lista esta Vacia")
    def ultimoElemento(self):
        if self.vacia() == False:
            return self.__items[self.__tope - 1]




                                                               ##correr todos los otros elementos que le siguen una posicion anterior

