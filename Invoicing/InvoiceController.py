from Invoice import Invoice
import matplotlib.pyplot as plt

invoices = []

def addInvoice(id, d, nif, paid, base, vat, producto, cantidad):
    
    l = ((producto, cantidad))
    inv = Invoice(id, d, nif, paid, base, vat, l)
    invoices.append(inv)
    
def notPaid():
    notpaid = []
    for inv in invoices:
        if inv.getPaid() == False:
            notpaid.append(inv)
    return notpaid

def yesPaid():
    yespaid = []
    for inv in invoices:
        if inv.getPaid() == True:
            yespaid.append(inv)
    return yespaid

def pay(id):
    for inv in invoices:
        if inv.getId() == id:
            inv.setPaid(True)
            return "Invoice " , id , " paid."
        
def graphic():
    invoicesIds = []
    invoicesTotal = []
    
    for inv in invoices:
        invoicesIds.append(inv.getId())
        invoicesTotal.append(inv.getTotal())
    plt.bar(x = invoicesIds, height=invoicesTotal)
    plt.xlabel("Ids")
    plt.ylabel("Total")
    plt.show()