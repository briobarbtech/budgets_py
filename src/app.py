import utils.manage_data as manage_data



def manage_client():
    user_option = ''
    print("1) Mostrar clientes")
    print("2) Agregar clientes")
    user_option = input('Ingrese una opción o X para salir: ').upper()
    if user_option == "1":
        manage_data.show_clients()
    elif user_option == "2":
        manage_data.add_client()

def main():
    user_option = ''
    while user_option != "X":
        print("1) Clientes")
        print("2) Vendedores")
        print("3) Vehículos")
        print("4) Ventas")
        user_option = input("Ingrese una opción o X para salir: ").upper()
        if user_option == "1":
           manage_client()   
        elif user_option == "2":
            manage_data.show_seller()
        elif user_option == "3":
            manage_data.show_vehicle()
        elif user_option == "4":
            manage_data.generate_purchase_summary()
main()