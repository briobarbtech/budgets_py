import csv

### Función para almacenar los productos en un archivo csv
def save_products():
    with open('productos.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
    
        # Opcional: Escribir la cabecera del CSV
        escritor_csv.writerow(["ID", "Producto", "Precio"])
    
        # Escribir cada fila de products en el archivo CSV
        escritor_csv.writerows(products)
    print("El archivo 'productos.csv' ha sido guardado correctamente.")
### Función para leer los archivos desde un archivo csv
def read_products():
    products = []
    with open('productos.csv', mode='r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
    
        # Saltar la cabecera si existe
        next(lector_csv)
    
        # Añadir cada fila al array products
        for fila in lector_csv:
            # Convertir los tipos de datos (ID a int y Precio a float)
            products.append([int(fila[0]), fila[1], float(fila[2])])
    return products


budget = []                                         ### Array donde se almacenan los prespuestos
client_list = [["41418471","Brian Barquesi", ""]]   ### Array de clientes
products = read_products()
#save_products()
##  Funciones del cliente ###
def add_client():
    client_name = input("Ingrese el nombre del nuevo cliente: ")
    client_id = input("Ingrese el DNI: ")
    client_list.append([client_id,client_name])

def choose_client():
    show_elements(client_list)
    client_choosed = input("Ingrese el DNI del cliente que desea crear prespuesto: ")
    return client_list[find_user_by_id(client_list,client_choosed)]

def find_user_by_id(clients, id):
    for client in clients:
        if client[0] == id:
            return clients.index(client)
    return None    

### Funciones del presupuesto ###
def create_budget():
    client = choose_client()
    id = len(budget)
    show_elements(products)
    new_budget = []
    current_id = ""
    while current_id != "G":
        show_elements(new_budget)
        current_id = input("Escribe el id de un producto para agregarlo o G para terminar y guardar, o X para salir sin guardar: ").upper()
        if current_id != "G" and current_id != "X":
            new_budget.append(products[int(current_id)-1])
        elif current_id == "X":
            break
        
    if current_id == "G":
        budget.append([client,new_budget])
    elif current_id == "X":
        pass

def show_budgets(budgets):
    for i in range(len(budgets)):
        print(f'{i}')

### Funciones generales ###
def show_elements(list):
    print("ID | Nombre |")
    for i in range(len(list)):
        print(f'{list[i][0]} {list[i][1]} ${list[i][2]}')

### MAIN ###
def main():
    action = ""
    while action != "X":
        print("1: Crear presupuesto")
        print("2: Ver productos")
        print("3: Ver presupuestos")
        action = input("Qué desea hacer? X para salir: ").upper()
        if action == "1":
            create_budget()
        elif action == "2":
            show_elements(products)
        elif action == "3":
            ## TODO: function to see budgets
            print(budget)
        elif action == "X":
            break

        
main()