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
    return tmplt_dict

def export_to_compose(version, services, compose_path):
    exported_dic = create_template()
    def insert_parameter():
        exported_dic["version"] = version
    insert_parameter()
    return exported_dic
print(export_to_compose("3.1", "", ""))
