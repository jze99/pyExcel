from flet import *
from test import addPath
    

def viewsHendler(page):
    
    def on_dialog_result(e: FilePickerResultEvent):
        if e.files == None:
            return
        value_path=e.files[0].path
        textPath.value = value_path
        addPath(value_path, drp)
        textPath.update()
        drp.update()
        
    file_picker = FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)
        
    textPath=TextField(
        label="Path",
        height=40,
        width=300,
        border_color="#F05941",
        read_only=True,
        value="Выберите Ecxel файл",
        text_size=12,
        multiline=False,
        expand=1,
        dense=True,
        on_focus=lambda _: file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["xlsx"]
        ),
    )
    
    textColumn=TextField(
        label="столбец",
        height=40,
        width=90,
        border_color="#F05941",
        text_size=12,
        value="A"
    )    
    textRowChec=TextField(
        label="строка",
        height=40,
        width=90,
        border_color="#F05941",
        text_size=12,
        value="1"
    )
    
    drp=Dropdown(
        height=50,
        width=90,
        text_size=12,
        border_color="#F05941",
        expand=1,
    )
    
    def clicAddTicet(e):
        page.go('/log')
        
    def returnMain(e):
        page.go('/')
        
    return {
        '/':View(
            route='/', 
            controls=[
               FloatingActionButton(icon=icons.ADD,on_click=clicAddTicet, bgcolor = "#F05941"),
               
            ],
            bgcolor="#22092C",
            auto_scroll=True
        ),  
        '/log':View(
            route='/log', 
            controls=[
                Row(
                    controls=[
                        IconButton(
                            icon=icons.ARROW_BACK_ROUNDED,
                            icon_size=40,
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=10),
                                    color="#F05941"
                                ),
                            on_click=returnMain  
                        ),
                        Column(
                            controls=[
                                #главная часть 
                                Row(
                                    controls=[
                                        textPath,
                                        IconButton(
                                            content=Image(
                                                src="image/ecxel_icon.png",
                                                color="#F05941",
                                                height=40,
                                                width=40,
                                                fit=ImageFit.CONTAIN
                                            ),
                                            on_click=lambda _: file_picker.pick_files(
                                                allow_multiple=False,
                                                allowed_extensions=["xlsx"]
                                            ),
                                            style=ButtonStyle(
                                                shape=RoundedRectangleBorder(radius=10),
                                                color="#F05941"
                                            ),
                                        ),
                                        
                                    ],
                                    alignment=MainAxisAlignment.CENTER,
                                ),
                                Row(
                                    controls=[
                                        drp
                                    ],    
                                ),
                                Row(
                                    controls=[
                                        textColumn,
                                        Text(
                                            height=40,
                                            value="столбец с которой будет считываться значение вниз",
                                            expand=1,
                                            size=12,
                                        )
                                    ],
                                    alignment=MainAxisAlignment.START,
                                ),
                                Row(
                                    controls=[
                                        textRowChec,
                                        Text(
                                            height=40,
                                            value="строка с которой будет считываться значение вниз",
                                            expand=1,
                                            size=12,
                                        )
                                    ]
                                ),
                            ],
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            expand=1,
                            auto_scroll=True
                        ),
                    ],
                    alignment=MainAxisAlignment.START,
                    vertical_alignment=CrossAxisAlignment.START,
                ),
                FloatingActionButton(
                        icon=icons.ARROW_FORWARD_SHARP,
                        on_click=clicAddTicet,
                        bgcolor = "#F05941"
                ),
            ],
            bgcolor="#22092C"
        )
    }