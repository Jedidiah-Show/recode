def flatten(items):
    if items == []:
        return items
    if isinstance(items[0], list):
        return flatten(items[0]) + flatten(items[1:])
    return items[:1] + flatten(items[1:])

def group_by(items, key_fn):
    new_dict = {}
    for item in items:
        key = key_fn(item)
        new_dict[key] = new_dict.get(key, []) + [item]
    return new_dict

def combined(items):
    items = flatten(items)
    items = group_by(items, lambda w: w[0])
    return items
print(group_by(["apple", "avocado", "banana"], lambda w: w[0]))
print(flatten([1, [2, [3, [4]], 5]]))
print(combined([["apple", "avocado"], ["banana"], [["cherry"]]]))
