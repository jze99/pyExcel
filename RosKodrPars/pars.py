from xml.etree import ElementTree as elem
from data import Object


newObjets=[]

def parsPath(pathDatadd:str):
    
    newObjets.clear()
    
    if pathDatadd == "":
        exit()
    
    tree = elem.parse(pathDatadd)
    root = tree.getroot()
    
    for child in root.iter("base_data"):
        for chaild in child:
            if(chaild.tag == "land_records"):
                land_records = chaild
                for land_record in land_records:
                    x=[]
                    y=[]
                    errorRate=[]
                    for common_dataChild in land_record.iter("common_data"):
                        cadNumber=common_dataChild[1].text
                        view = common_dataChild[0][1].text
                    for squareChild in land_record.iter("area"):
                        square = squareChild[0].text
                    for xChild in land_record.iter("x"):
                        x.append(xChild.text)
                    for yChild in land_record.iter("y"):
                        y.append(yChild.text)
                    for errorChild in land_record.iter("delta_geopoint"):
                        errorRate.append(errorChild.text)
                    if x:
                        x.pop()
                        y.pop()
                    if errorRate:
                        errorRate.pop()
                    newObjets.append(Object(view=view, cadNumber=cadNumber, errorRate=errorRate, x=x, y=y, square=square))

            if(chaild.tag == "build_records"):
                build_records=chaild
                for build_record in build_records:
                    x=[]
                    y=[]
                    errorRate=[]
                    for common_dataChild in build_record.iter("common_data"):
                        cadNumber=common_dataChild[1].text
                        view = common_dataChild[0][1].text
                    for squareChild in build_record.iter("area"):
                        square = squareChild.text
                    for xChild in build_record.iter("x"):
                        x.append(xChild.text)
                    for yChild in build_record.iter("y"):
                        y.append(yChild.text)
                    for errorChild in build_record.iter("delta_geopoint"):
                        errorRate.append(errorChild.text)
                    if x:    
                        x.pop()
                        y.pop()
                    if errorRate:
                        errorRate.pop()
                    newObjets.append(Object(view=view, cadNumber=cadNumber, errorRate=errorRate, x=x, y=y, square=square))

            if(chaild.tag == "construction_records"):
                construction_records=chaild
                for construction_record in construction_records:
                    x=[]
                    y=[]
                    errorRate=[]
                    for common_dataChild in construction_record.iter("common_data"):
                        cadNumber=common_dataChild[1].text
                        view = common_dataChild[0][1].text
                    for squareChild in construction_record.iter("area"):
                        square = squareChild.text
                    for xChild in construction_record.iter("x"):
                        x.append(xChild.text)
                    for yChild in construction_record.iter("y"):
                        y.append(yChild.text)
                    for errorChild in construction_record.iter("delta_geopoint"):
                        errorRate.append(errorChild.text)
                    if x:
                        x.pop()
                        y.pop()
                    if errorRate:
                        errorRate.pop()
                    newObjets.append(Object(view=view, cadNumber=cadNumber, errorRate=errorRate, x=x, y=y, square=square))

            if(chaild.tag == "object_under_construction_records"):
                object_under_construction_records=chaild
                for object_under_construction_record in object_under_construction_records:
                    x=[]
                    y=[]
                    errorRate=[]
                    for common_dataChild in object_under_construction_record.iter("common_data"):
                        cadNumber=common_dataChild[1].text
                        view = common_dataChild[0][1].text
                    for squareChild in object_under_construction_record.iter("area"):
                        square = squareChild.text
                    for xChild in object_under_construction_record.iter("x"):
                        x.append(xChild.text)
                    for yChild in object_under_construction_record.iter("y"):
                        y.append(yChild.text)
                    for errorChild in object_under_construction_record.iter("delta_geopoint"):
                        errorRate.append(errorChild.text)
                    if x:
                        x.pop()
                        y.pop()
                    if errorRate:
                        errorRate.pop()
                    newObjets.append(Object(view=view, cadNumber=cadNumber, errorRate=errorRate, x=x, y=y, square=square)) 