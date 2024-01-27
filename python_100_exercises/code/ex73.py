import pandas

data = pandas.read_csv("sampledata.txt")

data_2 = data * 2

data_2.to_csv("sampledata2.txt", index=None)