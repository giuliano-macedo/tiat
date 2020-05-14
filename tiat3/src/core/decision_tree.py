from pandas import read_csv
from collections import namedtuple, defaultdict
from math import log2


def entropy(negatives_length: int, positives_length: int):
    total = negatives_length + positives_length
    p_plus = positives_length / total
    p_negative = negatives_length / total
    return -(p_plus * log2(p_plus)) - (p_negative * log2(p_negative))


class Tree:
    def __init__(
        self, sn=[], sp=[], children=[], gain=0, label="", parent_edge_label=""
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

    def __repr__(self):
        return f"Tree({self.sn},{self.sp},{self.children},{self.gain},{self.label})"

    def __str__(self):
        return repr(self)


Example = namedtuple("Example", ["attributes", "label"])


class DecisionTree:
    def __init__(self, fname: str):
        df = read_csv(fname)
        self.attributes = list(df.keys())
        assert self.attributes.pop(-1) == "label"
        self.examples = [Example(t[0:-1], bool(t[-1])) for t in df.values]
        self.attr_values = self._get_attr_values()

        best_candidate = max(
            (self._build_node(i, self.examples) for i in range(len(self.attributes))),
            key=lambda t: t.gain,
        )

        print(best_candidate.label, best_candidate.gain)
        for children in best_candidate.children:
            print(children.parent_edge_label, children.is_leaf())
        exit()

        self.tree = self._id3(self.atributes, self.examples)

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
        if attr_index != None:
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
        # print("entropy_s", entropy_s)
        # print("attribute", attribute)

        children = []

        sum_ = 0
        for attr_value in self.attr_values[attribute]:
            sn, sp = self._find_p_where(examples, attribute_index, attr_value)
            children.append(Tree(sn, sp, parent_edge_label=attr_value))
            # DUNNO if is corect
            e = 0 if (len(sn) == 0 or len(sp) == 0) else entropy(len(sn), len(sp))
            sum_ += (len(sn + sp) / len(examples)) * e

        gain = entropy_s - sum_

        return Tree(examples_negatives, examples_positives, children, gain, attribute)

    def _id3(self, attributes, examples):
        return Tree()
