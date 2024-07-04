import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self.idMap={}


    def getAnni(self):
        return DAO.getAnno()


    def creaGrafo(self, anno, giorni):
        nodi= DAO.getNodi()
        for n in nodi:
            self.idMap[n.id]=n
            self._grafo.add_node(n)

        for e in DAO.getArchi(anno, giorni):
            self._grafo.add_edge(self.idMap[e[0]], self.idMap[e[1]], weight= e[2])


    def getSommaPesi(self):
        self.somPesiNodi = []
        for n in self._grafo.nodes:
            somma=0
            for n1 in self._grafo[n]:
                somma+= self._grafo[n][n1]['weight']
            self.somPesiNodi.append((n.id,somma))
        return self.somPesiNodi


    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

