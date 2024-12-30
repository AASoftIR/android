import toga
from toga.style import Pack
from toga.style.pack import CENTER, COLUMN

class MyApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=10))

        self.button = toga.Button('Go to AASoft', on_press=self.open_url, style=Pack(padding=10))
        main_box.add(self.button)

        self.main_window = toga.MainWindow(self.name)
        self.main_window.content = main_box
        self.main_window.show()

    def open_url(self, widget):
        import webbrowser
        webbrowser.open('https://aasoft.ir')

def main():
    return MyApp('My BeeWare App', 'org.beeware.myapp')

if __name__ == '__main__':
    main().main_loop()
