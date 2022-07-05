Python 3.10.4 (main, Apr  2 2022, 09:04:19) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
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

    


service1 = Service('db', 'postgres', 
KeyboardInterrupt
KeyboardInterrupt


name = 'db'
                   
image= 'postgres'
                   
volumes = ['db_data:/var/lib/postgresql/data', '/test/test1:/usr/share/data']
                   
environment = {
    'postgres_db': 'mapi',
    'postgres_user': 'mapi_user',
    'postgres_password': 's3cret'}
                   


for k, v in environment.items():
    print(f'{k}={v}')

                   
postgres_db=mapi
postgres_user=mapi_user
postgres_password=s3cret

expose = []
                   
ports = {'5432': '5432'}
                   
ports
                   
{'5432': '5432'}
s = Service(name, image, 'exec startup.sh', volumes, expose, ports, environment)
                   
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#23>", line 1, in <module>
TypeError: Service.__init__() missing 1 required positional argument: 'depends_on'
s = Service(name, image, 'exec startup.sh', volumes, expose, ports, environment, [])
                   


s.as_dict()
                   
{'name': 'db', 'image': 'postgres', 'command': 'exec startup.sh', 'volumes': ['db_data:/var/lib/postgresql/data', '/test/test1:/usr/share/data'], 'expose': [], 'ports': {'5432': '5432'}, 'environment': {'postgres_db': 'mapi', 'postgres_user': 'mapi_user', 'postgres_password': 's3cret'}, 'depends_on': []}
for k, v in s.as_dict().items():
                   print(k, ':', v)

                   
name : db
image : postgres
command : exec startup.sh
volumes : ['db_data:/var/lib/postgresql/data', '/test/test1:/usr/share/data']
expose : []
ports : {'5432': '5432'}
environment : {'postgres_db': 'mapi', 'postgres_user': 'mapi_user', 'postgres_password': 's3cret'}
depends_on : []
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
    def depend(service):
        self.depends_on.append(service)

        
s = Service(name, image, 'exec startup.sh', volumes, expose, ports, environment, [])
s1 = Service('myservice' , image, 'exec startup.sh', volumes, expose, ports, environment, [])
s2 = Service('yourservice' , image, 'exec startup.sh', volumes, expose, ports, environment, [])

s.depend(s1)
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#39>", line 1, in <module>
TypeError: Service.depend() takes 1 positional argument but 2 were given
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
    def depend(self, service):
        self.depends_on.append(service)

        
s = Service(name, image, 'exec startup.sh', volumes, expose, ports, environment, [])
s1 = Service('myservice' , image, 'exec startup.sh', volumes, expose, ports, environment, [])
s2 = Service('yourservice' , image, 'exec startup.sh', volumes, expose, ports, environment, [])
s.depend(s1)
s.depend(s2)

for k, v in s.as_dict().items():
    print(k, ':', v)

    
name : db
image : postgres
command : exec startup.sh
volumes : ['db_data:/var/lib/postgresql/data', '/test/test1:/usr/share/data']
expose : []
ports : {'5432': '5432'}
environment : {'postgres_db': 'mapi', 'postgres_user': 'mapi_user', 'postgres_password': 's3cret'}
depends_on : [<__main__.Service object at 0x7f01ef293070>, <__main__.Service object at 0x7f01ef292710>]
