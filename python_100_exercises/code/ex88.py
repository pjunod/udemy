import pandas

file = pandas.read_csv("countries_by_area.txt")

file['Result'] = file['population_2013']/file['area_sqkm']

print(file.sort_values(['Result']).iloc[-5:])
