from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import webbrowser

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        Window.clearcolor = (0, 0, 0, 1)  # Dark background
        btn = Button(text='Click Me', size_hint=(None, None), size=(200, 100))
        btn.bind(on_press=self.open_website)
        layout.add_widget(btn)
        return layout

    def open_website(self, instance):
        webbrowser.open('https://aasoft.ir')

if __name__ == '__main__':
    MyApp().run()
