class Encuesta:
    '''------------------------------------------------------------------------------------------------------
    # Atributos
    ------------------------------------------------------------------------------------------------------'''

    rangoedad = [(0-17), (18-54), (55, float('inf'))]
    estadocivil = ["casado", "soltero"]
    valoropinion = list (range(11))
    totalopiniones = 0
    opiniones = {}

    '''-----------------------------------------------------------------------------------------------------
    # Metodos
    -----------------------------------------------------------------------------------------------------'''

    # Constructor

    def __init__(self):
        self.rangoedad = [(0-17), (18-54), (55, float('inf'))]
        self.estadocivil = ["casado", "soltero"]
        self.valoropinion = list (range(11))
        self.totalopiniones = 0
        self.opiniones = {}

    def getRangoEdad(self):
        return self.rangoedad
    
    def getEstadoCivil(self):
        return self.estadocivil
    
    def getValorOpinion(self):
        return self.valoropinion
    
    def getTotalOpiniones(self):
        return self.totalopiniones
    
    def getOpiniones(self):
        return self.opiniones
    
    def consultarPromedioTotalDeLaEncuesta(self):
        return sum(self.getValorOpinion()) / self.getTotalOpiniones()
    
    def consultarNumeroTotalDeOpinionesRecogidas(self):
        return self.getTotalOpiniones()
    
    def agregarOpinion(self, rango_edad, estado_civil, valor_opinion):
        if rango_edad in self.getRangoEdad() and estado_civil in self.getEstadoCivil() and valor_opinion in self.getValorOpinion():
            self.totalopiniones += 1
        else:
            print("Rango de edad o estado civil no valido")

    def consultarValorParcial(self, rango_edad, estado_civil):
        valor = (rango_edad, estado_civil)
        opiniones = self.opiniones.get(valor, [])
        if not opiniones:
            return 0
        return sum(opiniones) / len(opiniones)