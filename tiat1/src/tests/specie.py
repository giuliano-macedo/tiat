import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))

from core import Graph,Specie

def test_crossover(p1,p2,expected_o1,expected_o2,cut_points=None):
	o1,o2=p1.crossover(p2,cut_points)
	assert((o1.genes==expected_o1) and (o2.genes==expected_o2))
def test_cut_points_generation(n):
	mid=n//2
	for first_point in range(1,mid):
		for second_point in range(mid,n):
			l=["X"]*n
			l.insert(first_point,"|")
			l.insert(second_point+1,"|")

			print((first_point,second_point)," ".join(l))

print("for 9")
test_cut_points_generation(9)
print("-"*48)
print("for 6")
test_cut_points_generation(6)
print("-"*48)
graph=Graph("../graph.json")
cut_points=[3,7]
p1=Specie(graph,[1,2,3,4,5,6,7,8,9])
p2=Specie(graph,[4,5,2,1,8,7,6,9,3])

p3=Specie(graph,[9,3,7,8,2,6,5,1,4])



test_crossover(p1,p2,[2,1,8,4,5,6,7,9,3],[3,4,5,1,8,7,6,9,2],cut_points)

print(p1.crossover(p1,cut_points))
