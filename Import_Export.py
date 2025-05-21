import csv

IMPORT_FILE = "import.csv"
EXPORT_FILE = "export.csv"
BILLING_FILE = "billing.csv"


def write_csv(file_name, data, mode="a"):
    with open(file_name, mode, newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)


def read_csv(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def owner_create():
    section = input("Enter section (import/export/billing): ").lower()
    if section == "import":
        item = input("Enter item name: ")
        quantity = input("Enter quantity: ")
        price = input("Enter price: ")
        write_csv(IMPORT_FILE, [item, quantity, price])
    elif section == "export":
        item = input("Enter item name: ")
        quantity = input("Enter quantity: ")
        price = input("Enter price: ")
        write_csv(EXPORT_FILE, [item, quantity, price])
    elif section == "billing":
        customer_name = input("Enter customer name: ")
        item = input("Enter purchased item: ")
        quantity = input("Enter quantity: ")
        price = input("Enter price: ")
        write_csv(BILLING_FILE, [customer_name, item, quantity, price])
    else:
        print("Invalid section!")

def owner_update():
    print("Owner can update records manually in CSV files.")

def owner_delete():
    print("Owner can delete records manually in CSV files.")

def owner_read():
    section = input("Enter section to read (import/export/billing): ").lower()
    if section == "import":
        read_csv(IMPORT_FILE)
    elif section == "export":
        read_csv(EXPORT_FILE)
    elif section == "billing":
        read_csv(BILLING_FILE)
    else:
        print("Invalid section!")

def dealer_create():
    item = input("Enter item name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    write_csv(IMPORT_FILE, [item, quantity, price])

def customer_read():
    read_csv(BILLING_FILE)

def main():
    role = input("Enter your role (owner/dealer/customer): ").lower()
    
    if role == "owner":
        action = input("Enter action (create/update/delete/read): ").lower()
        if action == "create":
            owner_create()
        elif action == "update":
            owner_update()
        elif action == "delete":
            owner_delete()
        elif action == "read":
            owner_read()
        else:
            print("Invalid action!")
    
    elif role == "dealer":
        dealer_create()
    
    elif role == "customer":
        customer_read()
    
    else:
        print("Invalid role!")

main()
