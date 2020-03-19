import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
from core import Pool,Graph
import numpy as np

np.random.seed(42)

graph=Graph("../graph.json")

pool=Pool(graph,10,.65,.01)
print("initial pop")
for specie,p in zip(pool.species,pool.ps):
	print(specie.genes,specie.cost,round(p*100,2))

for i in range(500):
	print(pool.gen,pool.best.cost)
	pool.step()