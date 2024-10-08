from utils.read_csv import read_csv
from utils.write_csv import write_csv

def show_clients():
    clients = read_csv('client')
    for client in clients:
        show_a_client(client)

def show_a_client(client):
    print(f'ID: {client[3]} | CUIL: {client[1]} | Nombre: {client[0]}')

def show_vehicle():
    vehicles = read_csv('vehicle')
    for vehicle in vehicles:
        show_a_vehicle(vehicle)

def show_a_vehicle(vehicle):
            print(f'ID: {vehicle[4]} | Nombre: {vehicle[0]} | Modelo: {vehicle[1]} | Precio: {vehicle[2]} | Descripción: {vehicle[3]}')

def show_seller():
    sellers = read_csv('seller')
    for seller in sellers:
        show_a_seller(seller)

def show_a_seller(seller):
    print(f'ID: {seller[2]} | CUIL: {seller[1]} | Nombre: {seller[0]}')

def get_client_by_id(id):
    client_list = read_csv('client')
    for client in client_list:
        if client[3] == id:
            return client
        
def get_seller_by_id(id):
    seller_list = read_csv('seller')
    for seller in seller_list:
        if seller[2] == id:
            return seller
        
def get_vehicle_by_id(id):
    vehicle_list = read_csv('vehicle')
    for vehicle in vehicle_list:
        if vehicle[4] == id:
            return vehicle


def generate_purchase_summary():
    orders_list = read_csv('order')
    
    for order in orders_list:
        vehicle = get_vehicle_by_id(order[0])
        show_a_vehicle(vehicle)
        print("-----------------------------")
        seller = get_seller_by_id(order[1])
        show_a_seller(seller)
        print("-----------------------------")
        client = get_client_by_id(order[2])
        show_a_client(client)
        print("-----------------------------")
        print(order[3])
        print("_____________________________________________________")

def add_client():
    clients = read_csv('client')
    name = input('Ingrese el nombre y apellido: ')
    cuil = input('Ingrese el DNI xx-xxxxxxxx-x: ')
    address = input('Ingrese la dirección: ')
    id = f"C{len(clients) + 1:03}"
    clients.append([name,cuil,address,id])
    write_csv('client',clients)