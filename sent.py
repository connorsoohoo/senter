from __future__ import absolute_import, division

import csv
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

from builtins import range, str, zip
from datetime import datetime
from io import open
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# --- examples -------
sentences = []
output = []
fileName = 'caltech.csv'
# first row is timestamp, second row is confession

# df = pd.read_csv(fileName, header=0, sep=u",", index_col=None)

# sentences = df.as_matrix
df = pd.read_csv(fileName, header=None, sep=u",", index_col=None)
sentences = df[1].tolist()
timestamps = df[0].tolist()
# with open(fileName) as f:
#     lines = f.readlines()
#     for line in lines:
#         sentences.append(line.split(',', 1))
        # print(sentences[1])

# with open(fileName) as csvDataFile:
#     csvReader = csv.reader(csvDataFile)
#     for row in csvReader:
#         sentences.append([row[0], row[1]])
print(len(sentences))
# print("zero is" + sentences[0])
# print(sentences)
# print("one is " + sentences[1])
analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    # if (len(sentence) >= 2):
    result = []
    result.append(sentence)
            # print("{:-<65} {}".format(sentence[1], str(vs)))

    vs = analyzer.polarity_scores(sentence)
    # print(str(vs))

    result.append(str(vs['compound']))
    result.append(str(vs['pos']))
    result.append(str(vs['neg']))
    result.append(str(vs['neu']))



    output.append(result)
        # print(sentence)
        # print("{:-<65} {}".format(sentence[1], str(vs)))

i = 0
for time in timestamps:
    output[i].append(time)
    i += 1
    
# print(len(output))
# print(output)

# res = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']]
my_df = pd.DataFrame(output, columns = ["confession", "compound", "positive", "negative", "neutral", "timestamp"])
my_df.to_csv('out.csv', index=False, header=True)