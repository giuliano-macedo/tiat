import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
from random import shuffle
from core import Graph

def test_path(path,expected=True):
	print("path:")
	graph.print_path(path)
	try:
		ans=graph.tsp_weight(path)
	except Exception as e:
		if expected:
			raise e
		ans="failed"
	print("cost:",ans)

graph=Graph("../graph.json")
print(graph.get_names_pretty())
print(graph.edges)
print("-"*48)
path=list(range(1,graph.n))
test_path(path)
for _ in range(20):
	shuffle(path)
	test_path(path)
test_path([0]*graph.n,False)

test_path([2, 3, 4, 5, 0, 1])
