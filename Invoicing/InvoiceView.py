import InvoiceController
from datetime import datetime

cont = 1

while True:
    print("1.- Add Invoice")
    print("2.- List not paid invoices: All and by Customer NIF")
    print("3.- List paid invoices: All and by Customer NIF")
    print("4.- Pay invoice")
    print("5.- Exit")
    print("6.- Grafica")
    
    option = int(input("Introduce una opcion: "))
    
    if option == 5:
        break
    
    if option == 1:
        id = cont
        d = datetime.now()
        nif = input("Introduce el nif: ")
        paid = False
        base = float(input("Introduce la base: "))
        vat = float(input("Introduce el vat: "))
        producto = input("Introduce el producto: ")
        cantidad = input("Introduce la cantidad: ")
        
        InvoiceController.addInvoice(id, d, nif, paid, base, vat, producto, cantidad)
        cont+= 1
        
    if option == 2:
        notpaid = InvoiceController.notPaid()
        print("Not Paid:")
        for inv in notpaid:
            print(inv.getId(), inv.getNif(), inv.getDate(), inv.getPaid(), inv.getTotal(), inv.getInvoicelines(),end="\n")
            
    if option == 3:
        yespaid = InvoiceController.yesPaid()
        print("Paid:")
        for inv in yespaid:
            print(inv.getId(), inv.getNif(), inv.getDate(), inv.getPaid(), inv.getTotal(), inv.getInvoicelines(),end="\n")
            
    if option == 4:
        InvoiceController.pay(int(input("Introduce el id de la factura a pagar: ")))
        
    if option == 6:
        InvoiceController.graphic()