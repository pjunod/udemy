import pandas
import matplotlib.pylab

data = pandas.read_csv("sampledata.txt")

data.plot(x='x', y='y', kind='scatter')

matplotlib.pylab.show()