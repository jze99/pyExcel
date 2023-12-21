class MifObject:
    def __init__(self, CadNumber:str, x, y, square):
        self.CadNumber = CadNumber
        self.x = x.copy()
        self.y = y.copy()
        self.square = square
class KPTObject:
    def __init__(self, CadNumber:str=None, view:str=None, square=None):
        self.CadNumber = CadNumber 
        self.view = view
        self.square = square
        self.x=[]
        self.y=[]
        self.errorRate=[]
        self.methodDetermination=[]
        self.source=[]
    
    def appedt(self, _x=None, _y=None, _errorRate=None, _methodDetermination=None, _source=None,):
        self.x=_x.copy()
        self.y=_y.copy()    
        self.errorRate=_errorRate.copy()    
        self.methodDetermination=_methodDetermination.copy()
        self.source=_source.copy()
class GeodesyObject:
    def __init__(self, x, y, errorRate, methodDetermination, source):
        self.x=x
        self.y=y
        self.errorRate=errorRate
        self.methodDetermination=methodDetermination
        self.source=source
class SupObject:
    def __init__(self, CadNumber, view, squareMIF, squareKPT):
        self.CadNumber = CadNumber
        self.view = view
        self.squareMIF = squareMIF
        self.squareKPT = squareKPT
        self.deviations = round((float(squareMIF)/float(squareKPT))*100-100, 2)
        self.x=[]
        self.y=[]
        self.errorRate=[]
        self.methodDetermination=[]
        self.sourse=[]
        
    def ader(self ,x, y, errorRate, methodDetermination, sourse):
        self.x.append(x)
        self.y.append(y)
        self.errorRate.append(errorRate)
        self.methodDetermination.append(methodDetermination)
        self.sourse.append(str(sourse))
        
        
NewMifCadObject = []

NewKPTCadObject = []

NewGeodesyObject = []

NewSuperObject=[]
