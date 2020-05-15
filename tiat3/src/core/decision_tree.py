from pandas import read_csv
from collections import namedtuple, defaultdict
from math import log2
from .tree import Tree


def entropy(negatives_length: int, positives_length: int):
    total = negatives_length + positives_length
    p_plus = positives_length / total
    p_negative = negatives_length / total
    return -(p_plus * log2(p_plus)) - (p_negative * log2(p_negative))


Example = namedtuple("Example", ["attributes", "label", "id"])


class DecisionTree:
    def __init__(self, fname: str):
        df = read_csv(fname)
        self.attributes = list(df.keys())
        assert self.attributes.pop(-1) == "label"
        self.examples = [
            Example(attributes=t[0:-1], label=bool(t[-1]), id=i)
            for i, t in enumerate(df.values)
        ]
        self.attr_values = self._get_attr_values()

        self.tree = self._id3(self.examples)

    def _get_attr_values(self):
        ans = defaultdict(set)
        for example in self.examples:
            for attr_name, attr_value in zip(self.attributes, example.attributes):
                ans[attr_name].add(attr_value)
        ans = {k: sorted(list(v)) for k, v in ans.items()}
        return ans

    def _find_p_where(
        self, examples: list, attr_index: int = None, attr_value: str = None
    ):
        sp = []
        sn = []
        if attr_index != None:  # if it is None, compute for S
            examples = (
                example
                for example in examples
                if example.attributes[attr_index] == attr_value
            )
        for example in examples:
            if example.label:
                sp.append(example)
            else:
                sn.append(example)
        return sn, sp

    def _build_node(self, attribute_index, examples):
        """
        builds a node and compute its gain
        """
        examples_negatives, examples_positives = self._find_p_where(examples)
        entropy_s = entropy(len(examples_negatives), len(examples_positives))
        attribute = self.attributes[attribute_index]

        children = []

        sum_ = 0
        for attr_value in self.attr_values[attribute]:
            sn, sp = self._find_p_where(examples, attribute_index, attr_value)
            new_children = Tree(sn, sp, parent_edge_label=attr_value)
            # DUNNO if is corect
            e = 0 if new_children.is_leaf() else entropy(len(sn), len(sp))
            if e == 0:
                new_children.label = len(sp) != 0
            sum_ += ((len(sn) + len(sp)) / len(examples)) * e
            children.append(new_children)

        gain = entropy_s - sum_

        return Tree(examples_negatives, examples_positives, children, gain, attribute)

    def _id3(self, examples, visited_attributes=None):
        if visited_attributes == None:
            visited_attributes = set()
        new_node, attr_i = max(
            (
                (self._build_node(i, examples), i)
                for i, _ in enumerate(self.attributes)
                if i not in visited_attributes
            ),
            key=lambda t: t[0].gain,
        )
        visited_attributes.add(attr_i)
        no_non_leaf_nodes = sum(
            1 for children in new_node.children if not children.is_leaf()
        )

        # if no_non_leaf_nodes > 1:
        #     # DUNNO what do here
        #     raise RuntimeError("Unexpected error")
        new_node.children = new_node.children[::-1]
        for i, children in enumerate(new_node.children):
            if children.is_leaf():
                continue
            new_children = self._id3(children.s, visited_attributes)
            new_children.parent_edge_label = children.parent_edge_label
            new_node.children[i] = new_children
        return new_node
