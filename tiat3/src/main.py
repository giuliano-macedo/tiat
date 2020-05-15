from core import DecisionTree
from tempfile import gettempdir

dt = DecisionTree("dataset_aula.csv")
# dt = DecisionTree("dataset_trabalho.csv")

dot = dt.tree.to_graphviz()

dot.render(
    "decision_tree",
    directory=gettempdir(),
    format="pdf",
    view=True,
    cleanup=True,
    quiet_view=True,
)
