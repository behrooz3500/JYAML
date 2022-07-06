name = 'db'                 
image= 'postgres'        
volumes = ['db_data:/var/lib/postgresql/data', '/test/test1:/usr/share/data']  
environment = {
    'postgres_db': 'mapi',
    'postgres_user': 'mapi_user',
    'postgres_password': 's3cret'}
expose = [8000, 8080]                
ports = {'5432': '5432'}
commands = 'exec startup.sh'
depends_on = []
s = [name, image, commands, volumes, expose, ports, environment, depends_on]
s1 = [s]
s2 = ['new', image, 'stay with mee', volumes, expose, ports, environment, depends_on]
s4 = ["new2", image, commands, volumes, expose, ports, environment, depends_on]
s3 = [s, s2, s4]