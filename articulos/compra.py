import locale

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self,alimento):
        id = str(alimento.cod)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "articulo_id": alimento.cod, 
                "nombre": alimento.nombre,
                "precio": str (alimento.precio),
                "cantidad": 1,
                "total": alimento.precio,
                }
        else:
            for key, value in self.carrito.items():
                if key==alimento.cod:
                    if alimento.stock <= value['cantidad']:
                        break
                    else:
                        value["cantidad"] = value["cantidad"]+1
                        value["precio"] = alimento.precio
                        value["total"]= value["total"] + alimento.precio
                        break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, alimento):
        id = alimento.cod
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,alimento):
        for key, value in self.carrito.items():
            if key==alimento.cod:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- alimento.precio
                if value["cantidad"] < 1:   
                    self.eliminar(alimento)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
