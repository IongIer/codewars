from collections import Counter, OrderedDict


class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj


def mix(s1, s2):
    s1_counter = Counter(c for c in s1 if c.islower() and s1.count(c) > 1)
    s2_counter = Counter(c for c in s2 if c.islower() and s2.count(c) > 1)
    union = OrderedDict((s1_counter | s2_counter).most_common())
    mix = ""
    for k in union:
        if union[k] == s1_counter[k] and union[k] != s2_counter[k]:
            mix += "1" + ":" + union[k] * k + "/"
        elif union[k] == s2_counter[k] and union[k] != s1_counter[k]:
            mix += "2" + ":" + union[k] * k + "/"
        else:
            mix += "=" + ":" + union[k] * k + "/"
    if not mix:
        return mix
    mixed = mix[:-1].split("/")
    return "/".join(sorted(mixed, key=lambda x: (reversor(len(x)), x[0], x)))
