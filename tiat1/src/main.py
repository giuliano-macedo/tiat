import argparse
import matplotlib.pyplot as plt
from itertools import permutations
from core import Graph,Specie,Pool
import numpy as np

def probabiliy(s):
	n=float(s)
	if not (0<=n<=100):
		raise RuntimeError("Value must be a probability in percentage")
	return n/100
parser=argparse.ArgumentParser()
parser.add_argument("-p","--population_size",type=int,default=5)
parser.add_argument("-c","--crossover_rate",type=probabiliy,default=.65)
parser.add_argument("-m","--mutation_rate",type=probabiliy,default=.5)
parser.add_argument("-s","--seed",type=int,default=42)

args=parser.parse_args()

np.random.seed(args.seed)

graph=Graph("graph.json")

pool=Pool(
	graph,
	args.population_size,
	args.crossover_rate,
	args.mutation_rate
)
print(pool.mutation_rate)
gloabl_minimum=min(Specie(graph,list(sol)).cost for sol in permutations(range(1,6)))

best_costs=[pool.best.cost]
while pool.best.cost!=gloabl_minimum:
	pool.step()
	best_costs.append(pool.best.cost)

plt.plot(range(0,len(best_costs)),best_costs)
plt.xlabel("Generation")
plt.ylabel("Best Cost")

plt.show()