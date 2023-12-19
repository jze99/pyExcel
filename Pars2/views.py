from flet import *
import os
import time
from unloadingMif import unloading
from unloadingKPT import readKPT
from unloadingGeodesy import readSheets,readGeodesy
from comparison import start
from discharge import Discharge
from CadObject import NewGeodesyObject, NewKPTCadObject, NewMifCadObject, NewSuperObject

def CheckPath(path: str, TextField:TextField):
    if os.path.isfile(path):
        TextField.value=path
        TextField.update()
    elif os.path.exists(path):
        TextField.value=path
        TextField.update()
    else:
        TextField.value = "Не правиьный путь"
        TextField.update()
        exit()

def viewsHendler(page): 
    
    def savePath(path:str):      
        f = open("data/path.txt", "w", encoding='utf-8')
        f.write(path)
        f.close()
    
    def CheckEcxelPath(e):
        if(CheckEcxel.value):
            savePath(path=pathParsDirectori.value)
        else:
            savePath("") 
            
    def LoadPath(_parsSheets:Dropdown):
        file = open("data/path.txt", "r", encoding='utf-8')
        content = file.read()
        if not os.path.isfile(content):
            content = ""
            return content
        file.close()
        _parsSheets.options.clear()
        _parsSheets.options.append(dropdown.Option("Новый лист"))
        for sheet in readSheets(pathDirectori=content):
            _parsSheets.options.append(dropdown.Option(str(sheet)))
        if _parsSheets.options:
            _parsSheets.value=_parsSheets.options[0].key
        
        return content
        
    def OnDialogResultMif(e: FilePickerResultEvent):
        NewMifCadObject.clear()
        if e.path == None:
            return
        else:
            CheckPath(path=e.path, TextField= pathMifDirectori)
            exit()
    
    def OnDialogResultKPT(e: FilePickerResultEvent):
        NewKPTCadObject.clear()
        if e.files == None:
            return
        else:
            CheckPath(path=e.files[0].path, TextField= pathKPTDirectori)
            exit()
            
    def OnDialogResultGeodesy(e: FilePickerResultEvent):
        NewGeodesyObject.clear()
        geodesySheets.options.clear()
        if e.files == None:
            return
        else:
            CheckPath(path=e.files[0].path, TextField= pathGeodesyDirectori)
            for sheet in readSheets(pathDirectori=pathGeodesyDirectori.value):
                geodesySheets.options.append(dropdown.Option(str(sheet)))
            if geodesySheets.options:
                geodesySheets.value=geodesySheets.options[0].key
            geodesySheets.update()
            exit()
            
    def OnDialogResultPars(e: FilePickerResultEvent):
        parsSheets.options.clear()
        parsSheets.options.append(dropdown.Option("Новый лист"))
        if e.files == None:
            return
        else:
            CheckPath(path=e.files[0].path, TextField= pathParsDirectori)
            if CheckEcxel.value:
                savePath(e.files[0].path)
            for sheet in readSheets(pathDirectori=pathParsDirectori.value):    
                parsSheets.options.append(dropdown.Option(str(sheet)))
            if parsSheets.options:
                parsSheets.value=parsSheets.options[0].key
            parsSheets.update()
            exit()
    
    filePickerMif = FilePicker(on_result=OnDialogResultMif)
    page.overlay.append(filePickerMif)
    filePickerKPT = FilePicker(on_result=OnDialogResultKPT)
    page.overlay.append(filePickerKPT)
    filePickerGeodesy = FilePicker(on_result=OnDialogResultGeodesy)
    page.overlay.append(filePickerGeodesy)
    filePickerPars = FilePicker(on_result=OnDialogResultPars)
    page.overlay.append(filePickerPars)

    pathMifDirectori=TextField(
        label="Выберите папку с mif файлами",
        height=40,
        width=300,
        border_color="#F05941",
        read_only=True,
        value="",
        text_size=12,
        multiline=False,
        expand=1,
        dense=True,
        on_focus=lambda _: filePickerMif.get_directory_path(),
    )
     
    pathKPTDirectori=TextField(
        label="Выберите файл КПТ",
        height=40,
        width=300,
        border_color="#F05941",
        read_only=True,
        value="",
        text_size=12,
        multiline=False,
        expand=1,
        dense=True,
        on_focus=lambda _: filePickerKPT.pick_files(
            allow_multiple=False,
            allowed_extensions=["xlsx"]
        ),
    )
    
    pathGeodesyDirectori=TextField(
        label="Выберите файл Геодезия",
        height=40,
        width=300,
        border_color="#F05941",
        read_only=True,
        value="",
        text_size=12,
        multiline=False,
        expand=1,
        dense=True,
        on_focus=lambda _: filePickerGeodesy.pick_files(
            allow_multiple=False,
            allowed_extensions=["xlsx"]
        ),
    )
    
    geodesySheets=Dropdown(
        label = "лист геодезии",
        border_color = "#F05941",
        height=60
    )
    
    parsSheets=Dropdown(
        label = "лист для переноса данных",
        border_color = "#F05941",
        height=60
    )
    
    pathParsDirectori=TextField(
        label="Выберите файл для сохранения",
        height=40,
        width=300,
        border_color="#F05941",
        read_only=True,
        value=LoadPath(_parsSheets=parsSheets),
        text_size=12,
        multiline=False,
        expand=1,
        dense=True,
        on_focus=lambda _: filePickerPars.pick_files(
            allow_multiple=False,
            allowed_extensions=["xlsx"]
        ),
    )
            
    CheckEcxel = Checkbox(
        label="Сохранить расположение Excel файла ?",   
        value=True,
        on_change=CheckEcxelPath,
        fill_color={
            MaterialState.DEFAULT:"#F05941"            
        },           
    )
    def nextParsCont():
        if not unloading(pathDirectori=pathMifDirectori.value):
            time.sleep(1)
            return False

        if not readKPT(pathDirectori=pathKPTDirectori.value):
            time.sleep(1)
            return False

        if not readGeodesy(pathDirectori=pathGeodesyDirectori.value, _sheet=geodesySheets.value):
            time.sleep(1)
            return False
        start()
        Discharge(path=pathParsDirectori.value, _sheet=parsSheets.value)
        return True
    
    def nextPars(e):
        page.go("/log")
        if nextParsCont():
            page.go("/")
        else:
            page.go("/isc")
        NewMifCadObject.clear()
        NewKPTCadObject.clear()
        NewGeodesyObject.clear()
        NewSuperObject.clear()
        return None

    
    addParsButton = FloatingActionButton(icon=icons.ARROW_RIGHT_ALT,on_click=nextPars, bgcolor = "#F05941")
    
    def BeckPars(e):
        page.go("/")
    
    BeckParsButton = FloatingActionButton(icon=icons.ARROW_RIGHT_ALT,on_click=BeckPars, bgcolor = "#F05941")
       
    return {
        '/isc':View(
            route='/isc', 
            controls=[
                Column(
                    controls=[
                        Text(
                            "Произошла ошибка, введены неверные данные, перепроверьте файлы вставленные в поля",
                            size=45,
                            color="#F05941",
                            weight=FontWeight.NORMAL,
                            text_align=TextAlign.START,
                        ),
                    ],
                    expand=1,
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
                BeckParsButton,
            ],    
            bgcolor="#22092C"
        ),
        '/':View(
            route='/', 
            controls=[
                Column(
                    controls=[
                        Row(
                            controls=[
                                pathMifDirectori,
                                IconButton(
                                    icon=icons.ADD_BOX_SHARP,
                                    style=ButtonStyle(
                                        color="#F05941",
                                        shape=RoundedRectangleBorder(radius=10)
                                    ),
                                    icon_size=40,
                                    on_click=lambda _: filePickerMif.get_directory_path()
                                ),
                            ],
                        ),
                        Row(
                            controls=[
                                pathKPTDirectori,
                                IconButton(
                                    icon=icons.ADD_BOX_SHARP,
                                    style=ButtonStyle(
                                        color="#F05941",
                                        shape=RoundedRectangleBorder(radius=10)
                                    ),
                                    icon_size=40,
                                    on_click=lambda _: filePickerKPT.pick_files(
                                        allow_multiple=False,
                                        allowed_extensions=["xlsx"]
                                    ),
                                ),
                            ],
                        ),
                        Row(
                            controls=[
                                pathGeodesyDirectori,
                                IconButton(
                                    icon=icons.ADD_BOX_SHARP,
                                    style=ButtonStyle(
                                        color="#F05941",
                                        shape=RoundedRectangleBorder(radius=10)
                                    ),
                                    icon_size=40,
                                    on_click=lambda _: filePickerGeodesy.pick_files(
                                        allow_multiple=False,
                                        allowed_extensions=["xlsx"]
                                    ),
                                ),
                            ],
                        ),
                        Row(
                            controls=[
                                geodesySheets
                            ],
                        ),
                        Row(
                            controls=[
                                pathParsDirectori,
                                IconButton(
                                    icon=icons.ADD_BOX_SHARP,
                                    style=ButtonStyle(
                                        color="#F05941",
                                        shape=RoundedRectangleBorder(radius=10)
                                    ),
                                    icon_size=40,
                                    on_click=lambda _: filePickerPars.pick_files(
                                        allow_multiple=False,
                                        allowed_extensions=["xlsx"]
                                    ),
                                ),
                            ],
                        ),
                        Row(
                            controls=[
                                parsSheets,
                            ],
                        ),
                        Row(
                            controls=[
                                CheckEcxel,    
                            ],
                        ),
                    ],
                ),
                addParsButton,
            ],
            bgcolor="#22092C",
            auto_scroll=True
        ),  
        '/log':View(
            route='/log', 
            controls=[
                Column(
                    controls=[
                        Text(
                            "Пожалуйста подождите",
                            size=50,
                            color="#F05941",
                            weight=FontWeight.NORMAL,
                            text_align=TextAlign.CENTER,
                        ),
                    ],
                    expand=1,
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
            ],    
            bgcolor="#22092C"
        ),
    }
