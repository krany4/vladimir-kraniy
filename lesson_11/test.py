def merge_dicts(*dicts):
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))