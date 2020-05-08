from core import DE
import numpy as np
import random
import matplotlib.pyplot as plt

np.random.seed(42)
random.seed(42)

max_gen=100
popsize=5
feat_size=5

pop=[]
for i in range(popsize):
	pop.append(np.random.rand(feat_size)*5)

de=DE(
	init_pop=pop,
	fitness_callable=np.sum,
	cr=0.5,
	f=1.2
)
pop_costs=[]
for _ in range(max_gen):
	pop_costs.append(de.pop_cost())
	de.step()

plt.plot(pop_costs)

plt.xlabel("Generation")
plt.ylabel("Cost")
plt.show()