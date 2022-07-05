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
#s = Service(name, image, commands, volumes, expose, ports, environment)