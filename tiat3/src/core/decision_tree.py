from pandas import read_csv
from collections import namedtuple, defaultdict
from math import log2


def entropy(negatives_length: int, positives_length: int):
    total = negatives_length + positives_length
    p_plus = positives_length / total
    p_negative = negatives_length / total
    return -(p_plus * log2(p_plus)) - (p_negative * log2(p_negative))


class Tree:
    def __init__(self, sn=[], sp=[], children=[]):
        self.sn = sn
        self.sp = sp
        self.children = children


Example = namedtuple("Example", ["attributes", "label"])


class DecisionTree:
    def __init__(self, fname: str):
        df = read_csv(fname)
        self.attributes = list(df.keys())
        assert self.attributes.pop(-1) == "label"
        self.examples = [Example(t[0:-1], bool(t[-1])) for t in df.values]
        self.attr_values = self._get_attr_values()

        gains = []

        for i in range(len(self.attributes)):
            gains.append((self.attributes[i], self._gain(i, self.examples)))

        gains.sort(key=lambda t: t[1])
        print(*gains[::-1], sep="\n")
        exit()

        self.tree = self._id3(atributes, examples)

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

    def _gain(self, attribute_index, examples):
        entropy_s = entropy(*(len(p) for p in self._find_p_where(examples)))
        attribute = self.attributes[attribute_index]
        # print("entropy_s", entropy_s)
        # print("attribute", attribute)

        sum_ = 0
        for attr_value in self.attr_values[attribute]:
            sn, sp = self._find_p_where(examples, attribute_index, attr_value)
            e = 0 if (len(sn) == 0 or len(sp) == 0) else entropy(len(sn), len(sp))
            sum_ += (len(sn + sp) / len(examples)) * e
        return entropy_s - sum_

    def _id3(self, attributes, examples):
        return Tree()