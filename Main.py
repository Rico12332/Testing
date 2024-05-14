from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from datetime import datetime

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        date_time_label = Label(text=datetime.now().strftime('%A, %B %d, %Y %I:%M %p'), font_size='20sp')
        layout.add_widget(date_time_label)

        for i in range(4):
            button = Button(text=f'Button {i+1}', font_size='14sp')
            layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyApp().run()