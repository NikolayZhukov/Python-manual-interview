import copy

original1 = [1, 2, [3, 4]]
shallow_copy = original1.copy()
print(shallow_copy)
print(id(shallow_copy))
print(id(original1))

original2 = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original2)
print(deep_copy)
print(id(deep_copy))
print(id(original2))



# def myEmptyFunc():
#     pass
#
# myEmptyFunc()