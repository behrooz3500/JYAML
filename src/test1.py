import json
import os 



path = ("/home/amirmm4d/Behrooz/Projects/JYAML")

py_dict = {"staff" : 
                [
                        {"first" : "behrooz",
                        "last" : "ghorbani"
                        },
                        {"first" : "mehrdad",
                        "last":"ghorbani"
                        }
                ]
        }
py_string = ('{"staff" : [{"first" : "behrooz","last" : "ghorbani"},{"first" : "mehrdad","last":"ghorbani"}]}')

json_string1 = json.loads(py_string)
json_string2 = json.dumps(py_dict, indent = 3)



with open("test.json",'w+') as jfile:
        json.dump(py_dict, jfile, indent = 3)
        jfile.close()
