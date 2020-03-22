from core import Graph,Pool
import numpy as np
from args import get_args
from tqdm import tqdm
import pickle

args=get_args(p=1000,m=0.01)

np.random.seed(args.seed)

graph=Graph("states.json","Mato Grosso do Sul")

with open("best_extra.p","rb") as f:
	initial=pickle.load(f)
pool=Pool(
	graph,
	args.population_size,
	args.crossover_rate,
	args.mutation_rate,
	initial
)
no_iterations=int(5e4)

last_best=None

for i in tqdm(range(no_iterations)):
	pool.step()
	if last_best==None or last_best.cost!=pool.best.cost:
		tqdm.write(f"gen {pool.gen:4} cost:{pool.best.cost:10}")
		last_best=pool.best
		with open("best_extra.p","wb") as f:
			pickle.dump(pool.best.genes,f)
pool.best.print(pretty=False)
