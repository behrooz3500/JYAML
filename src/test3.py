import test2 as t


path = "test_yaml.yaml"
data = t.yaml_reader(path)
data2 = t.yaml_all_reader(path)

data3 = data2

for i in data3:
    print(type(i))
