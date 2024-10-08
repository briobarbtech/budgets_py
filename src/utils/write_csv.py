import csv
def write_csv(name, data):
    with open(f'{name}.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        csv_file_writer = csv.writer(csv_file)
        
        csv_file_writer.writerow(["Nombre y Apellido", "Cuil", "Dirección","ID"])
        
        csv_file_writer.writerows(data)
    print(f"El archivo '{name}.csv' ha sido guardado correctamente.")
    
