from os import replace


products = [0,1,2,3]
quantprod = [10, 4, 0, 9]
prices = [9.99, 19.9, 14.99, 4.99]

cash = 0.0
#quantProducts = 0
#priceProductos = 0.0


#Functions
def getPriceProduct(code):
    return products[code]

def getQuantityProduct(code):
    return quantprod[code]

def getDetailProduct(code):
    return quantprod[code], prices[code]

def getCash():
    return cash

def addQuantProduct(code, quant):
    quantprod[code] = quant

def setPriceProduct(code, price):
    prices[code] = price

def saleProduct(code):
    global cash
    if quantprod[code] > 0:
        quantprod[code] = quantprod[code] -1
        cash = cash + prices[code]
        return True
    else:
        return False
    
def replaceProduct(code, quantity):
    global cash
    tot = prices[code] * quantity
    if cash < (tot * 0.8):
        return False
    else:
        cash = cash - tot
        quantprod[code] = quantprod[code] + quantity
        return True

def getFullStock():
    print("[Code - Units - Price]")
    for i in products:
        print("[", i, " - ", quantprod[i], " - ", prices[i],"]")

while True:
    print("1.-Show full store detail")
    print("2.-Sales")
    print("3.-Replace")
    print("4.-Change price of product")
    print("5.-Exit")
    print(getCash())

    option = int(input())
    
    if option == 1:
        getFullStock()

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