from core import Graph,Pool
import numpy as np
from args import get_args
from tqdm import tqdm
import pickle

args=get_args(p=100,m=0.01)

np.random.seed(args.seed)

graph=Graph("states.json","Mato Grosso do Sul")

pool=Pool(
	graph,
	args.population_size,
	args.crossover_rate,
	args.mutation_rate
)

times=[]
no_iterations=int(1e6)

for i in tqdm(range(no_iterations)):
	pool.step()
	tqdm.write(f"gen {pool.gen:4} cost:{pool.best.cost:10}")
with open("best_extra.p","wb") as f:
	pickle.dump(pool,f)
pool.best.print(pretty=False)
