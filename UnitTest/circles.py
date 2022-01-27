from math import pi


# for(name, _) in getmembers(pandas, isfunction):
#     if not name.startswith("_"):
#         if name in ["to_pickle"]:
#             print(name)

def circle_area(r):
    if type(r) not in [int, float]:
        raise ValueError("This is not type of Int or float")
    if r < 0:
        raise ValueError("The Radius can not be Negative Value")
    return pi * (r ** 2)

