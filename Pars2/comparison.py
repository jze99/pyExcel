import CadObject

def test(Mif, _i):
    try:
        for __i, Xmif in enumerate(Mif.x):
            o = False
            for Kpt in CadObject.NewKPTCadObject:
                for Xkpt in Kpt.x:
                    i = Kpt.x.index(Xkpt)
                    if float(Xmif) == float(Xkpt) and float(Mif.y[__i]) == float(Kpt.y[i]) and o == False and str(Mif.CadNumber) == str(Kpt.CadNumber):
                        CadObject.NewSuperObject[_i].ader(x=Xkpt, y=Kpt.y[i], errorRate=Kpt.errorRate[i], methodDetermination=Kpt.methodDetermination[i], sourse="ЕГРН")  
                        o = True
                        break
                    if float(Xmif) == float(Xkpt) and float(Mif.y[__i]) == float(Kpt.y[i]) and o == False:
                        CadObject.NewSuperObject[_i].ader(x=Xkpt, y=Kpt.y[i], errorRate=Kpt.errorRate[i], methodDetermination=Kpt.methodDetermination[i], sourse="КПТ")  
                        o = True
                        break
            for geo in CadObject.NewGeodesyObject:
                if float(Xmif) == float(geo.x) and float(Mif.y[__i]) == float(geo.y) and o == False:
                    CadObject.NewSuperObject[_i].ader(x=geo.x, y=geo.y, errorRate=geo.errorRate, methodDetermination=geo.methodDetermination, sourse="ГОДЕЗИЯ") 
                    o = True
                    break 
            if o == False:
                CadObject.NewSuperObject[_i].ader(x=Xmif, y=Mif.y[__i], errorRate=1, methodDetermination="картометрический метод", sourse="")
                continue
        return True
    except IndexError:
        return False
    
    

def start():
        for Mif in CadObject.NewMifCadObject:
            for cad in CadObject.NewKPTCadObject:
                if str(Mif.CadNumber) == str(cad.CadNumber):
                    CadObject.NewSuperObject.append(CadObject.SupObject(CadNumber=Mif.CadNumber, view=cad.view, squareKPT=cad.square, squareMIF=Mif.square,))
        for i, Mif in enumerate(CadObject.NewMifCadObject):                    
            if not test(Mif=Mif ,_i=i):
                continue
                                    
            