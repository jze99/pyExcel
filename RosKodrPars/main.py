from flet import *
from views import viewsHendler

def main(page: Page):
       
    page.window_min_height = 600
    page.window_height = 600
    page.window_min_width = 450
    page.window_width = 450
    page.title = "Парсер"
    
    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(viewsHendler(page)[page.route])
    
    page.on_route_change = route_change
    page.go('/')


app(target=main)