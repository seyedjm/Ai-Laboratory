import pandas as pd
import math
from collections import Counter


dadeha = "simple_cybersecurity_dataset.csv" 

df = pd.read_csv(dadeha)


print("=== dataset ma ===")
print(df)
print()

def entropy(labels):
    total = len(labels)
    counts = Counter(labels)

    ent = 0
    for label, c in counts.items():
        p = c / total
        ent -= p * math.log2(p)

    return ent

def information_gain(df, feature, target):
    total_entropy = entropy(df[target].tolist())
    total_len = len(df)

    values = df[feature].unique()
    weighted_entropy = 0

    for v in values:
        subset = df[df[feature] == v]
        weight = len(subset) / total_len
        weighted_entropy += weight * entropy(subset[target].tolist())

    return total_entropy - weighted_entropy

def id3(df, features, target):

    if len(df[target].unique()) == 1:
        return df[target].iloc[0]


    if len(features) == 0:
        return df[target].mode()[0]


    best_feature = None
    best_ig = -1

    for f in features:
        ig = information_gain(df, f, target)
        if ig > best_ig:
            best_ig = ig
            best_feature = f


    tree = {best_feature: {}}


    for v in df[best_feature].unique():
        subset = df[df[best_feature] == v]
        remaining_features = [f for f in features if f != best_feature]

        tree[best_feature][v] = id3(subset, remaining_features, target)

    return tree

features = ["attack_type", "attack_vector", "target_asset"]
target = "threat_level"

print("=== Total Entropy ===")
print(entropy(df[target].tolist()))
print()

print("=== Information Gain for each feature ===")
for f in features:
    print(f, "-> IG =", information_gain(df, f, target))
print()

print("=== Decision Tree (as dict) ===")
tree = id3(df, features, target)
print(tree)
