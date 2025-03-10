from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MeuLayout(BoxLayout):
    def on_button_click(self, instance):
        if instance.text == 'Vermelho':
            instance.background_color = 'green'
            instance.text = 'Sucesso!'
        
        elif instance.text == 'Azul':
            instance.background_color = 'black'
            instance.text = 'Dark mode ativado!'


class MeuApp(App):
    def build(self):
        return MeuLayout()


if __name__ == '__main__':
    MeuApp().run()