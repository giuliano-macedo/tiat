import argparse
def probabiliy(s):
	n=float(s)
	if not (0<=n<=100):
		raise RuntimeError("Value must be a probability in percentage")
	return n/100
def get_args(p=5,c=.65,m=.5,s=42):
	parser=argparse.ArgumentParser()
	parser.add_argument("-p",
		"--population_size",
		type=int,
		default=p,
		help=f"number of species per generation (default {p})"
	)
	parser.add_argument("-c",
		"--crossover_rate",
		type=probabiliy,
		default=c,
		help=f"probability of crossover per generation (default {c*100})"
	)
	parser.add_argument("-m",
		"--mutation_rate",
		type=probabiliy,
		default=m,
		help=f"probability of mutation per generation (default {m*100})"
	)
	parser.add_argument("-s",
		"--seed",
		type=int,
		default=s,
		help=f"initial seed (default {s})"
	)

	return parser.parse_args()