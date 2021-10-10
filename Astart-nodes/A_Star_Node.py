import json
with open('estrutura.json') as json_file:
    data = json.load(json_file)

#entrada de dados é com json organizado como
# nome da Cidade, nodos:(cidadaA:Distancia,CidadeB:Distancia pra B....)linha direta(distantciaPraDestinoFinal)

def nodeMenor(lista,nodeAux):
    nodeAux.Copia(lista[0])
    for node in lista:
        #print(node.name + ": "+ str(node.f) +" " + nodeAux.name + ":"+str(nodeAux.f))
        if node.f <= nodeAux.f:
            nodeAux = node
    return nodeAux

def nomesListaNodos(lista):
    retorno = []
    for node in lista:
        retorno.append(node.name)
    return retorno

def readHFromJson(String):
       return list(data[String].items())[1][1]


def getChildrenNameG(String):
    listaRetorno=[]
    for i in data[String]['nodes'].items():
        listaRetorno.append(i)
    return listaRetorno



class Node():
    def __init__(self,String,Parent):
        self.name=String
        self.parent=Parent
        self.h=readHFromJson(self.name)
        self.g=0
        self.f=0
        self.children=getChildrenNameG(self.name)

    def Copia(self,Node):
        self.name=Node.name
        self.parent=Node.parent
        self.g=Node.g
        self.h=Node.h
        self.f=Node.f
        self.children=Node.children

    def genChildren(self):
        listaRetorno =[]
        for kidInfo in self.children:
            newNodo = Node(kidInfo[0],self)
            newNodo.g =  kidInfo[1] + self.g
            newNodo.f = newNodo.h + newNodo.g
            listaRetorno.append(newNodo)
        return listaRetorno


def AStar(start,end):
    start_node= Node(start,None)
    end_node= Node(end,None)
    nodeAux= Node("Bucharest",None)
    nodeAux.f= 99999999
    open_list=[]
    closed_list=[]
    open_list.append(start_node)
    while len(open_list)>0:
        print("lista aberta: " + str(nomesListaNodos(open_list)) )
        print("lista fechada: " + str(nomesListaNodos(closed_list)) )
        current_node = nodeMenor(open_list,nodeAux)
        print("\n current node: " +current_node.name +"\n")
        open_list.remove(current_node)
        closed_list.append(current_node)
        print("lista aberta: " + str(nomesListaNodos(open_list)) )
        print("lista fechada: " + str(nomesListaNodos(closed_list)) )
        if current_node.name == end_node.name:
            print('achou')
            listaPath=[]
            while current_node != None:
                print(current_node.name)
                listaPath.append(current_node)
                current_node=current_node.parent
            return listaPath
        kids = current_node.genChildren()
        print("kids" + str(nomesListaNodos(kids)))
        for kid in kids:
            if kid.name in nomesListaNodos(closed_list):
                a=1
            else:
                if kid in nomesListaNodos(open_list):
                    print(kid.name)
                    for node in open_list:
                        if node.name == kid.name:
                            print(node.name+" == "+kid.name)
                            if kid.g < node.g:
                                node.Copia(kid)
                else:
                    open_list.append(kid)

inicio="Lugoj"
final="Bucharest"
a=AStar(inicio,final)

for i in range(len(a),0,-1):
    print(a[i-1].name+" g:"+str(a[i-1].g)+" h:"+str(a[i-1].h) + " f:" +str(a[i-1].f) )