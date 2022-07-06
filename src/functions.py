from re import L
import yaml
import json


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

        
###reading a yml file
def yaml_reader(filepath):
    with open(filepath, 'r') as yf:
        data = yaml.safe_load(yf)
    return data

###reading a yml file as a generator
def yaml_all_reader(filepath):
    with open(filepath, 'r') as yf:
        data = yaml.safe_load_all(yf)
    return data

###Exporting data to a yml file
def yaml_writer(filepath, data):
    with open(filepath, "w") as yf:
        yaml.dump(data, yf, sort_keys=False, Dumper=NoAliasDumper)

###Exporting data to a Json file
def file_writer(pathfile, data):
    with open (pathfile,'w+') as wr:
        json.dump(data, wr, indent=3)

###Creating template dictionaries
def create_template():

    tmplt_dict = {
        "version":"",
        "services":{
            "name":{
                "image":"",
                "container_name":"",
                "command":"",
                "volumes":[
                ],
                "expose":[
                ],
                "ports":[
                ],
                "environment":[
                ],
                "depends_on":[
                ],
            }
        }
    }

    tmplt_dict2 = {
        "version":"",
        "services":{         
            }
        }
    return tmplt_dict2

def tmplt_dict():

    list_of_outer_keys = ["version",
                         "services",
                         "volumes"
                         ]

    list_of_service_keys = ["image",
                            "container_name",
                            "command",
                            "volumes",
                            "expose",
                            "ports",
                            "environmnent",
                            "depends_on"
                            ]

    return list_of_outer_keys, list_of_service_keys