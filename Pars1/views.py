from flet import *
from pars import parsPath
from upload import uploadPath
import os

def checPath(path:str, Obj: TextField):
    if os.path.exists(path):
        return True
    else:
        Obj.value = "Файла не существует проверьте путь"
        Obj.update()
        savePath("")
        return False

def savePath(path:str):      
    f = open("data/path.txt", "w", encoding='utf-8')
    f.write(path)
    f.close()
    
def readPth():
    file = open("data/path.txt", "r", encoding='utf-8')
    content = file.read()
    file.close()
    return content


def viewsHendler(page):

    
    def OnDialogResultData(e: FilePickerResultEvent):
        if e.files == None:
            return
        value_path=e.files[0].path
        checPath(value_path, dataPath)
        dataPath.value = value_path
        dataPath.update()
        
    def OnDialogResultTabl(e: FilePickerResultEvent):
        if e.files == None:
            return
        value_path=e.files[0].path
        checPath(value_path, dataPath)
        tablPath.value = value_path
        if CheckEcxel.value == True:
            savePath(value_path)
        tablPath.update()
        
    filePickerTabl = FilePicker(on_result=OnDialogResultTabl)
    filePickerData = FilePicker(on_result=OnDialogResultData)
    page.overlay.append(filePickerTabl)
    page.overlay.append(filePickerData)
        
    dataPath=TextField(
        label="Выберите XMl документ",
        height=40,
        width=300,
        border_color="#F05941",
        read_only=True,
        value="",
        text_size=12,
        multiline=False,
        expand=1,
        dense=True,
        on_focus=lambda _: filePickerData.pick_files(
            allow_multiple=False,
            allowed_extensions=["xml"]
        ),
    )
    
    tablPath=TextField(
        label="Выберите Excel докумет с расширением xlsx",
        height=40,
        width=300,
        border_color="#F05941",
        read_only=True,
        value="",
        text_size=12,
        multiline=False,
        expand=1,
        dense=True,
        on_focus=lambda _: filePickerTabl.pick_files(
            allow_multiple=False,
            allowed_extensions=["xlsx"]
        ),
    )     
    
    def CheckEcxelPath(e):
        if(CheckEcxel.value):
            savePath(tablPath.value)
        else:
            savePath("") 
            
    CheckEcxel = Checkbox(
        label="Сохранить расположение Excel файла ?",   
        value=True,
        on_change=CheckEcxelPath,
        fill_color={
            MaterialState.DEFAULT:"#F05941"            
        },           
    )
    
    def nextPars(e):
        if checPath(path=dataPath.value, Obj=dataPath) and checPath(path=tablPath.value, Obj=tablPath):
            page.go('/log')
            addParsButton.disabled=False
            parsPath(dataPath.value)
            uploadPath(tablPath.value)
            addParsButton.disabled=True
            page.go('/')
        else:
            exit()
            
    addParsButton = FloatingActionButton(icon=icons.ARROW_RIGHT_ALT,on_click=nextPars, bgcolor = "#F05941")
        
    tablPath.value=readPth()
        
    return {
        '/':View(
            route='/', 
            controls=[
               Row(
                   controls=[
                       dataPath,
                       IconButton(
                           icon=icons.ADD_BOX,
                           icon_size=60,
                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=10),
                                color="#F05941"
                            ),
                            on_click=lambda _: filePickerData.pick_files(
                                allow_multiple=False,
                                allowed_extensions=["xml"]
                            ),
                       )
                    ],
               ),
               Row(
                   controls=[
                       tablPath,
                       IconButton(
                            icon=icons.ADD_BOX,
                            icon_size=60,
                            style=ButtonStyle(
                                color="#F05941",
                                shape=RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda _: filePickerTabl.pick_files(
                                allow_multiple=False,
                                allowed_extensions=["xlsx"]
                            ),
                       ),
                    ],
                ),
                Row(
                    controls=[
                        CheckEcxel
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
        )
    }
