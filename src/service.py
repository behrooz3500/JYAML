import functions as t
import testCases as tc
import yaml

class Service(object):
    """Service Model"""
    def __init__(
        self,
        name,
        image,
        command,
        volumes,
        expose,
        ports,
        environment,
        depends_on
    ):
        self.name = name
        self.image = image
        self.command = command
        self.volumes = volumes
        self.expose = expose
        self.ports = ports
        self.environment = environment
        self.depends_on = depends_on

    def as_dict(self):
        return {
            'name': self.name,
            'image': self.image,
            'command': self.command,
            'volumes': self.volumes,
            'expose': self.expose,
            'ports': self.ports,
            'environment': self.environment,
            'depends_on': self.depends_on
        }




def export_to_compose(version, services, compose_path):
    #Create a template dictionary
    exported_dic = t.create_template()

    #setting version
    exported_dic["version"] = version

    #setting parameters for  services
    for s in services:
        sec_dict = {s[0]:
                        {"image":s[1],
                        "container_name":s[0],
                        "command":s[2],
                        "volumes":s[3],
                        "expose":s[4],
                        "ports":s[5],
                        "environment":s[6],
                        "depends_on":s[7]
                        }
                    }
        print(sec_dict)
        #adding service parameters to the template dict
        exported_dic.get("services").update(sec_dict)
        #exported_dic["services"] = sec_dict
        #sec_dict.clear()

    #Exporting dict as a yml file
    t.yaml_writer(compose_path, exported_dic)


    
    
def export_to_compose2(version, services, compose_path):
    inner_dict = dict(zip(t.tmplt_dict()[1],services))
    outer_dict = dict.fromkeys(t.tmplt_dict()[0],{})
    outer_dict["version"] = version
    #outer_dict.get("services").update(services[0])
    #outer_dict.get("services").update(inner_dict)
    t.yaml_writer(compose_path, outer_dict)

#test case
services = tc.s3
compose_path = ("exported.yml")
export_to_compose("3.2",services,compose_path)
