import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
from core import Pool,Graph,Specie
import numpy as np
from itertools import permutations

np.random.seed(42)

graph=Graph("../graph.json")

pool=Pool(graph,10,.65,.01)
print("initial pop")
for specie,p in zip(pool.species,pool.ps):
	print(specie.genes,specie.cost,round(p*100,2))

gloabl_minimum=min(Specie(graph,list(sol)).cost for sol in permutations(range(1,6)))

print("global minimum",gloabl_minimum)

while pool.best.cost!=gloabl_minimum:
	pool.step()
print(f"took {pool.gen} generations to reach gloabl minimum cost")