class Conta:
    
    def __init__(self,numero,titular,saldo,limite):
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite
        
    
    def deposita(self,valor):
        self.saldo+=valor
        
    
    def saca(self,valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
    
    def extrato(self):
        print(f"Número: {self.numero} \n Saldo: {self.saldo} ")
    
    
    def transfere_para(self,destino,valor):
        retirou= self.saca(valor)
        if ( retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True

