import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'software enginner',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'data enginner',
    }
]

def create_client(client):
	global clients
	if client not in clients:
		clients.append(client)
	else:
		print("El cliente ya esta en la lista")

def list_clients():
    global clients
    for index, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = index,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position'],
        ))

def update_client(client_name, updated_name):
	global clients
	if client_name in clients:
		index = clients.index(client_name)
		clients[index] = updated_name
	else:
		print("El cliente no esta en la lista")

def delete_client(client_name):
	global clients
	if client_name in clients:
		clients.remove(client_name)
	else:
		print("El cliente no esta la lista")

def search_client(client_name):
	for client in clients:
		if client != client_name:
			continue
		else:
			return True

def _get_cliente_field(field_name):
    field = None
    while not field:
        field = input('Datos del cliente {}? '.format(field_name))
        if field == 'exit':
            field = None
            break
    if not field:
        sys.exit()
    return field

def _get_client_name():
	client_name = None
	while not client_name:
		client_name = input("Cual es el nommbre del cliente: ")
		if client_name == "exit":
			client_name = None
			break
	if not client_name:
		sys.exit()
	return client_name

def _print_welcome():
	print("Bienvenido")
	print("*" * 30)
	print("Opciones:")
	print("Create cliente [C]")
	print("Update client [U]")
	print("Delete client [D]")
	print("Search client [S]")

if __name__ == '__main__':
	_print_welcome()
	command = input()
	command = command.upper()
	if command == "C":
        client = {
            'name': _get_cliente_field('new name'),
            'company': _get_cliente_field('new company'),
            'email': _get_cliente_field('new email'),
            'position': _get_cliente_field('new position'),
        }
		create_client(client_name)
		list_clients()
	elif command == "L":
		list_clients()
	elif command == "U":
		client_name = _get_client_name()
		updated_client_name = input("Ingrese el nombre del cliente: ")
		update_client(client_name, updated_client_name)
		list_clients()
	elif command == "D":
		client_name = _get_client_name()
		delete_client(client_name)
		list_clients()
	elif command == "S":
		client_name = _get_client_name()
		found = search_client(client_name)
		if found:
			print("El cliente esta en la lista")
		else:
			print("{} no esta en la lista".format(client_name))
	else:
		print("Comando invalido")