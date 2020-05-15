from core import DecisionTree
from tempfile import gettempdir

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("dataset", type=str, choices=["aula", "trabalho"])
args = parser.parse_args()
dt = DecisionTree(
    "dataset_aula.csv" if args.dataset == "aula" else "dataset_trabalho.csv"
)


dot = dt.tree.to_graphviz()

dot.render(
    "decision_tree",
    directory=gettempdir(),
    format="pdf",
    view=True,
    cleanup=True,
    quiet_view=True,
)
