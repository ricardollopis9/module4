class Invoice:
    def __init__(self, id, date, nif, paid, base, vat, invoicelines):
        self.__id = id
        self.__date = date
        self.__nif = nif
        self.__paid = paid
        self.__base = base
        self.__vat = vat
        self.__total = base * vat
        self.__invoicelines = invoicelines
        
    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id
    
    def setDate(self, date):
        self.__date = date
    def getDate(self):
        return self.__date
    
    def setNif(self, nif):
        self.__nif = nif
    def getNif(self):
        return self.__nif
    
    def setPaid(self, paid):
        self.__paid = paid
    def getPaid(self):
        return self.__paid
    
    def setBase(self, base):
        self.__base = base
    def getBase(self):
        return self.__base
    
    def setVat(self, vat):
        self.__vat = vat
    def getVat(self):
        return self.__vat
    
    def getTotal(self):
        return self.__total
    
    def getInvoicelines(self):
        return self.__invoicelines