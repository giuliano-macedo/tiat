from core import Graph,Pool
import numpy as np
from args import get_args
from tqdm import tqdm
import pickle
import os

args=get_args(p=1000,m=0.01)

np.random.seed(args.seed)

graph=Graph("states.json","Mato Grosso do Sul")

initial=None

if os.path.isfile("best_extra.p"):
	with open("best_extra.p","rb") as f:
		initial=pickle.load(f)
pool=Pool(
	graph,
	args.population_size,
	args.crossover_rate,
	args.mutation_rate,
	initial
)

last_best=None
try:
	progress=tqdm(unit=" gen")
	while True:
		progress.update()
		pool.step()
		if last_best==None or last_best.cost!=pool.best.cost:
			tqdm.write(f"new best specie in gen {pool.gen:4} cost:{pool.best.cost:10}")
			last_best=pool.best
			with open("best_extra.p","wb") as f:
				pickle.dump(pool.best.genes,f)
except KeyboardInterrupt:
	print("\nexiting")

pool.best.print(pretty=False)
