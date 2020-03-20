import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))

from core import Specie,Graph
from itertools import permutations
graph=Graph("../graph.json")
for i in range(graph.n):
	start=graph.nodes[i]
	graph.startindex=i
	initial=list(set(range(graph.n))-{graph.startindex})

	gloabl_minimum=max(Specie(graph,list(sol)) for sol in permutations(initial))

	print(f"global minimum for {start:15}: cost={gloabl_minimum.cost} path={gloabl_minimum.genes}")
