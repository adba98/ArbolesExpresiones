# Arbol de expresiones (sin variable)
from Pila import Pila

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)
	
class Nodo():
    def __init__(self, val, izq=None, der=None):
        self.valor = val
        self.izq = izq
        self.der = der
		
if __name__ == "__main__":
	f = open ('expresiones.in','r')
	pf = f.read().split()
	print(pf)
	f.close()
	p = Pila()
	convertir(pf,p)
	fin = p.es_vacia
	f2 = open("expresiones.out","w")
	while(p.es_vacia() == False):
		f2.write(str(evaluar(p.desapilar()))+'\n')
	f2.close()
