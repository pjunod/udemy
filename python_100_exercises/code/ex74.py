import pandas

filea = pandas.read_csv("sampledata.txt")
fileb = pandas.read_csv("sampledata2.txt")

combined = pandas.concat([filea, fileb])

combined.to_csv("sampledatacombined.txt", index=None)