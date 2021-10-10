import json
with open('estrutura.json') as json_file:
	data = json.load(json_file)
	print data
	for p in data:
		print p


def nodeMenor(lista):
	nodeAux= lista[0]
	for node in lista:
		if node.f < nodeAux.f:
			nodeAux.Copia(node)
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
	def __init__(String,Parent):
		self.name=String
		self.parent=Parent
		self.h=readHFromJson(self.name)
		self.g=0
		self.f=0
		self.children=getChildrenNameG(self.name)

	def Copia(Node):
		self.name=Node.name
		self.parent=Parent
		self.g=Node.g
		self.h=Node.h
		self.f=Node.f
		self.children=Node.children

	def __eq__(self, other):
		return self.name == other.name


	def genChildren():
		listaRetorno =[]
		for kidInfo in self.children():
			newNodo = Node(kidInfo[0],self)
			newNodo.g =  kidInfo[1] + self.g
			newNodo.f = newNodo.h + newNodo.g
			listaRetorno.append(newNodo)
		return listaRetorno


def AStar(start,end):
	start_node= Node("",None)
	end_node= Node("",None)

	open_list=[]
	closed_list=[]

	open_list.append(start_node):

	while len(open_list)>0:
		current_node = nodeMenor(open_list)
		#remover
		open_list.remove(current_node)
		#adicionar
		closed_list.append(current_node)

		if current_node == end_node:
			listaPath=[]
			while current_node.parent != None:
				listaPath[:-1].append(current_node)
				current_node=current_node.parent
			return listaPath

		kids = current_node.genChildren()
		for kid in kids:

			if kid.name is in nomesListaNodos(closed_list):
				#nada
			else:
				if kid is in nomesListaNodos(open_list):
					for node in open_list:
						if node == kid:
							if kid.g < node.g:
								node.Copia(kid)
				else:
					open_list.append(kid)