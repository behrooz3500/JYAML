import test2 as t


path = ("docker-compose.yml")
data = t.yaml_reader(path)
t.file_writer("test.txt", data)


print(data)