import test2 as t
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
    tmplt_dict2 = {
        "version":"",
        "services":{         
            }
        }
    return tmplt_dict2


name = 'db'                 
image= 'postgres'        
volumes = ['db_data:/var/lib/postgresql/data', '/test/test1:/usr/share/data']  
environment = {
    'postgres_db': 'mapi',
    'postgres_user': 'mapi_user',
    'postgres_password': 's3cret'}
expose = []                
ports = {'5432': '5432'}
commands = 'exec startup.sh'
services = [name, image, commands, volumes, expose, ports, environment,[]]
compose_path = ("exported.yml")
def export_to_compose(version, services, compose_path):
    exported_dic = create_template()
    exported_dic["version"] = version
    sec_dict = {services[0]:
                    {"image":services[1],
                    "container_name":services[0],
                    "command":services[2],
                    "volumes":services[3],
                    "expose":services[4],
                    "ports":services[5],
                    "environment":services[6],
                    "depends_on":services[7]
                    }
                    
                }
    exported_dic["services"] = sec_dict
    print (exported_dic)
    
    t.yaml_writer(compose_path, exported_dic)

export_to_compose("3.2",services,compose_path)