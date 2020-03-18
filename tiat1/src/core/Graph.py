import json
import numpy as np
class Graph:
	def __init__(self,fname="graph.json"):
		with open(fname) as f:obj=json.load(f)
		self.nodes=obj["nodes"]
		self.n=len(self.nodes)
		self.edges=np.empty((self.n,self.n))
		self.edges[:]=np.nan
		for namei,namej,w in obj["edges"]:
			i=self.nodes.index(namei)
			j=self.nodes.index(namej)
			self.edges[i][j]=w
			self.edges[j][i]=w

	def get_names_pretty(self):
		ans=[]
		for name in self.nodes:
			name_splitted=name.split(" ")
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
			raise RuntimeError("invalid path")
		return ans

