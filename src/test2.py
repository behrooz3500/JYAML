import yaml


def yaml_reader(filepath):
    with open(filepath, 'r') as yf:
        data = yaml.safe_load(yf)
    return data

def yaml_all_reader(filepath):
    with open(filepath, 'r') as yf:
        data = yaml.safe_load_all(yf)
    return data


def yaml_writer(filepath, data):
    with open(filepath, "w") as yf:
        yaml.dump(data, yf)
