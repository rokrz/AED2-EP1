import csv
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import numpy as np

#Classe que representa os objetos do dict
class Lugar:
    def __init__(self,coord_x, coord_y):
        self.coordenada_x = int(coord_x)
        self.coordenada_y = int(coord_y)
        self.frequentadores = []
        
    def verifyCoord(self, coordX, coordY):
        if (int(coordX) == self.coordenada_x & int(coordY) == self.coordenada_y):
            return True
        else: return False
    
    def increaseFreq(self, id):
        self.frequentadores.append(id) 
        

#Funcao que cria uma chave dadas a coordenada x e a coordenada y
def creteStrid(x,y):
    return str(x)+'-'+str(y)


#O dict em si
places = {}

#le o csv
with open('OD_2017.csv') as csvfile:
    numberOfPlaces = 0
    readCSV = csv.reader(csvfile, delimiter = ',')
    next(readCSV)
    for row in readCSV:
        stridDefault = creteStrid(0,0)
        alreadyExists = False
        
        #Le a coordenada, verifica se a chave ja existe na lista, caso nao exista, cria uma chave nova e a insere
        strid = creteStrid(row[84],row[85])
        if (places.get(strid)is not None) & (strid is not stridDefault) :
            lugar = places.get(strid)
            lugar.increaseFreq(row[44])
            print('Increased Freq. count in '+strid)
            places[strid]=lugar
            alreadyExists = True
        elif(strid is not stridDefault):
            lugar = Lugar(row[84],row[85])
            lugar.increaseFreq(row[44])
            strid = creteStrid(row[84],row[85])
            places[strid] = lugar
            print('Added new Place to List '+strid)
            
        strid2 = creteStrid(row[88],row[89])
        if (places.get(strid2)is not None) & (strid2 is not stridDefault) :
            lugar = places.get(strid2)
            lugar.increaseFreq(row[44])
            print('Increased Freq. count in '+strid2)
            places[strid2]=lugar
            alreadyExists = True
        elif(strid2 is not stridDefault):
            lugar = Lugar(row[88],row[89])
            lugar.increaseFreq(row[44])
            places[strid2] = lugar
            print('Added new Place to List '+strid2)
            
        strid3 = creteStrid(row[92],row[93])
        if (places.get(strid3)is not None) & (strid3 is not stridDefault) :
            lugar = places.get(strid3)
            lugar.increaseFreq(row[44])
            print('Increased Freq. count in '+strid3)
            places[strid3]=lugar
            alreadyExists = True
        elif(strid3 is not stridDefault):
            lugar = Lugar(row[92],row[93])
            lugar.increaseFreq(row[44])
            places[strid3] = lugar
            print('Added new Place to List '+strid3)
            
        strid4 = creteStrid(row[96],row[97])
        if (places.get(strid4)is not None) & (strid4 is not stridDefault) :
            lugar = places.get(strid4)
            lugar.increaseFreq(row[44])
            print('Increased Freq. count in '+strid4)
            places[strid4]=lugar
            alreadyExists = True
        elif(strid4 is not stridDefault):
            lugar = Lugar(row[96],row[97])
            lugar.increaseFreq(row[44])
            places[strid4] = lugar
            print('Added new Place to List '+strid4)
            
        strid5 = creteStrid(row[100],row[101])
        if (places.get(strid5)is not None) & (strid5 is not stridDefault) :
            lugar = places.get(strid4)
            lugar.increaseFreq(row[44])
            print('Increased Freq. count in '+strid5)
            places[strid5]=lugar
            alreadyExists = True
        elif(strid5 is not stridDefault):
            lugar = Lugar(row[100],row[101])
            lugar.increaseFreq(row[44])
            places[strid5] = lugar
            print('Added new Place to List '+strid5)
            
            
            
#Remove lugar inexistente -> x =0, y=0
places.pop('0-0')

#Formata os dados para facilitar na criação do arquivo de saida
len(places.keys())
keys = places.keys()
values = places.values()
keysExtracted = []
valuesExtracted = []

#Escreve os dados de saída na forma: chave("coord_x-coord_y"), totalFrequentadores
f = open("results.csv", "a")
for k in keys:
    keysExtracted.append(k)
    valuesExtracted.append(len(places.get(k).frequentadores))
    print(k+', '+str(len(places.get(k).frequentadores)))
    f.write(k+', '+str(len(places.get(k).frequentadores))+';\n')
    
f.close()
