import test2 as t


path = ("docker-compose.yml")
data = t.yaml_reader(path)
print (type(data))
t.file_writer("test.txt", data)

t_dic = {"name":{"value":"3","value2":"n"}}
print(t_dic)