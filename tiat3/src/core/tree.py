import graphviz
from collections import deque


class Tree:
    def __init__(
        self, sn=[], sp=[], children=[], gain=0, label="", parent_edge_label=None
    ):
        self.sn = sn
        self.sp = sp
        self.s = sn + sp
        self.children = children
        self.gain = gain
        self.label = label
        self.parent_edge_label = parent_edge_label

    def is_leaf(self):
        return len(self.sn) == 0 or len(self.sp) == 0

    def is_root(self):
        return self.parent_edge_label == None

    def __repr__(self):
        return f"Tree(parent_edge_label={repr(self.parent_edge_label)},label={repr(self.label)},children={self.children})"
        # return f"Tree({self.sn},{self.sp},{self.children},{self.gain},{self.label})"

    def __str__(self):
        return repr(self)

    def to_graphviz(self):
        """
        Returns:
            (graphviz.Graph) 
        """
        stack = deque([self])
        ans = graphviz.Graph()
        while stack:
            tree = stack.popleft()
            ans.node(tree.label)
            for children in tree.children:
                if children.is_leaf():
                    id_ = str(id(children))
                    ans.node(id_, label="Sim!" if children.label else "Não.")
                    ans.edge(tree.label, id_, label=children.parent_edge_label)
                else:
                    stack.append(children)
                    ans.edge(
                        tree.label, children.label, label=children.parent_edge_label
                    )

        return ans
