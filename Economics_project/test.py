import pynance as pn
import pandas as pd
import numpy as np

apple_ = pn.data.get('IBM', '2024', '2025')

apple_.to_csv('ibm.csv')

apple = pd.read_csv('./ibm.csv')

prev = 0
x = 0
new = ["start"]
diff = []

appl = apple['Close'].to_list()

for i in appl:

    if x == 0:
        prev = i

    if i > prev:
        print("hi")
        new.append("1")
    elif i < prev: 
        print("low")
        new.append("0")

    diff.append(100 - (i / prev) * 100)

    prev = i
    x += 1

new.append("end")

print(new)

apple["Diff"] = diff
apple["isLarger"] = new

print(apple)

apple.to_csv("ibm.csv")