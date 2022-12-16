import random
import pandas as pd

class something:
    def __init__(self, something):
        self.something = something

    def hi():
        print("Hello World")



x = pd.DataFrame({"keys": ['a', 'b', 'c'], "values": [1, 1, 1]})
y = pd.DataFrame({"keys": ['a', 'c'], "values": [2, 2]})

keys = pd.merge(x["keys"], y["keys"], how="outer")

# print(x)
# print(y)

z = pd.merge(keys, y, on='keys', how='outer')
z = pd.merge(z, x, on='keys', how='outer')
z.index = ["red", "green", "blue"]

print(z)
