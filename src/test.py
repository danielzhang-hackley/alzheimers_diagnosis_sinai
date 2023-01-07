import random
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

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

# print(z)


x = np.array([[1, 2, 3], [4, 5, 6]])
print(np.argmax(x[0]))

# X = pd.read_csv(r'./data/X_expr.csv').drop(['Unnamed: 0', 'seqLibID'], axis=1).values
# y = pd.read_csv(r'./data/y_cog.csv').drop(['Unnamed: 0', 'seqLibID'], axis=1).values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)
# print(np.where(y_train == 'NoCognitiveImpairment')[0].shape[0])
# print(np.where(y_train == 'MildCognitiveImpairment')[0].shape[0])
# print(np.where(y_train == 'AD')[0].shape[0])

print(np.random.choice([1, 2, 3, 4, 5], 3, replace=False))

q = [1, 2, 3]

for i in q:
    pass  # i += 1

print(q[:-1])

