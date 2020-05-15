from core import DecisionTree

dt = DecisionTree("dataset1.csv")
print(dt.tree)

dot = dt.tree.to_graphviz()
dot.render("test", format="pdf")
