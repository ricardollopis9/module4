quantprod = {
    1 : 10,
    2 : 4,
    3 : 0,
    4 : 9
}
prices = {
    1 : 9.99,
    2 : 19.9,
    3 : 14.99,
    4 : 4.99,
}

cash = 0.0
#quantProducts = 0
#priceProductos = 0.0


#Functions
def getPriceProduct(code):
    return prices.get(code)

def getQuantityProduct(code):
    return quantprod.get(code)

def getDetailProduct(code):
    return quantprod.get(code), prices.get(code)

def getCash():
    return cash

def addQuantProduct(code, quant):
    quantprod[code] = {quant}

def setPriceProduct(code, price):
    prices[code] = {price}

def saleProduct(code):
    global cash
    if getQuantityProduct(code) > 0:
        quantprod[code] = getQuantityProduct(code) - 1
        cash = cash + getPriceProduct(code)
        return True
    else:
        return False
    
def replaceProduct(code, quantity):
    global cash
    tot = getPriceProduct(code) * quantity
    if cash < (tot * 0.8):
        return False
    else:
        cash = cash - tot
        quantprod[code] = getQuantityProduct(code) + quantity
        return True

def getFullStock():
    lista = []
    #print("[Code - Units - Price]")
    for i in quantprod.keys():
        lista.append((i, quantprod.get(i), prices.get(i)))
    return lista
        #print("[", i, " - ", quantprod.get(i), " - ", prices.get(i),"]") https://refloo.odoo.com/web#cids=1&action=251&model=account.journal&view_type=kanban&menu_id=176

    print(getCash())

while True:
    print("1.-Show full store detail")
    print("2.-Sales")
    print("3.-Replace")
    print("4.-Change price of product")
    print("5.-Exit")
    print(getCash())

    option = int(input())
    
    if option == 1:
        print("[Code - Units - Price]")
        print(getFullStock())

    elif option == 2:
        if saleProduct(int(input("Enter product code: "))):
            print("Successful sale!")
        else:
            print("Error, item does not exist or is out of stock!")

    elif option == 3:
        if replaceProduct(int(input("Enter product code: ")), int(input("Units to replace: "))):
            print("Correct Replacement!")
        else:
            print("There is no cash in the box to replace!")

    elif option == 4:
        setPriceProduct(int(input("Enter product code: ")), int(input("Enter the new price: ")))
        print("Price Updated!")

    elif option == 5:
        break