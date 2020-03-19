import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))

from core import Graph,Specie
import numpy as np

def test_crossover(p1,p2,expected_o1,expected_o2,cut_points=None):
	o1,o2=p1.crossover(p2,cut_points)
	assert((o1.genes==expected_o1) and (o2.genes==expected_o2))
def test_cut_points_generation(n):
	mid=n//2
	for first_point in range(1,mid+1):
		for second_point in range(first_point+1,n):
			l=["X"]*n
			l.insert(first_point,"|")
			l.insert(second_point+1,"|")

			print((first_point,second_point)," ".join(l))

np.random.seed(42)

print("for 9")
test_cut_points_generation(9)
print("-"*48)
print("for 5")
test_cut_points_generation(5)
print("-"*48)

cut_points=[5,8]
p1=Specie(None,[1,2,3,4,5,6,7,8,9],False)
p2=Specie(None,[9,8,7,6,5,4,3,2,1],False)

test_crossover(p1,p2,[9, 5, 4, 3, 2, 6, 7, 8, 1],[1, 5, 6, 7, 8, 4, 3, 2, 9],cut_points)

graph=Graph("../graph.json")

p1=Specie(graph,[1,2,3,4,5])
p2=Specie(graph,[5,4,3,2,1])


o1,o2=p1.crossover(p2)

for specie in (p1,p2,o1,o2):
	print("genes",specie.genes)
	print("fitnes",specie.fitness)
	print("after mutation")
	specie.mutate()
	print("genes",specie.genes)
	print("fitnes",specie.fitness)