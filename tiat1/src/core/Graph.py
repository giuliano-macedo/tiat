import json
import numpy as np
from unidecode import unidecode
class Graph:
	def __init__(self,fname="graph.json",start=None):
		self.fname=fname
		with open(self.fname) as f:obj=json.load(f)
		self.nodes=obj["nodes"]
		self.startindex=0 if start==None else self.nodes.index(start)
		self.n=len(self.nodes)
		self.edges=np.empty((self.n,self.n))
		self.edges[:]=np.nan
		for namei,namej,w in obj["edges"]:
			i=self.nodes.index(namei)
			j=self.nodes.index(namej)
			self.edges[i][j]=w

	def __repr__(self):
		return f"Graph({repr(self.fname)})"

	def get_names_pretty(self):
		ans=[]
		for name in self.nodes:
			name_splitted=unidecode(name).split(" ")
			if len(name_splitted)==1:
				ans.append(name[:3].lower())
			else:
				ans.append("".join((split[0] for split in name_splitted)))
		return ans

	def path_weight(self,path):
		ans=sum((
			self.edges[i][j] for i,j in zip(path,path[1:]) #iterate two in two
		))
		if np.isnan(ans):
			raise RuntimeError("invalid path",path)
		return ans

	def tsp_weight(self,path):
		
		ans=self.path_weight(path)

		ans+=self.edges[self.startindex][path[0]]
		ans+=self.edges[path[-1]][self.startindex]

		if np.isnan(ans):
			raise RuntimeError("invalid path",path)

		return ans

	def print_path(self,path,pretty=True,tsp=False):
		print(self.path_to_string(path,pretty,tsp))

	def path_to_string(self,path,pretty=True,tsp=False):
		names=self.get_names_pretty() if pretty==True else self.nodes
		if tsp:
			path=[self.startindex]+path+[self.startindex]
		return " -> ".join((names[i] for i in path))