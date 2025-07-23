import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class generator(GridLayout):
    def __init__(self, **kwargs):
        super(generator, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Hastalık ismi girin:'))
        self.Hastalık = TextInput(multiline=False)
        self.add_widget(self.Hastalık)

        self.add_widget(Label(text='Uygulanacak işlem:'))
        self.islem = TextInput(multiline=False)
        self.add_widget(self.islem)

        self.add_widget(Label(text='Hastanın kullandığı ilaç:'))
        self.ilac = TextInput(multiline=False)
        self.add_widget(self.ilac)

        self.buton = Button(text='Üret')
        self.buton.size_hint = (0.3, None)  
        self.buton.height = 40
        self.buton.bind(on_press=self.ekle)
        self.add_widget(self.buton)

        self.etiket = Label(
            text="Uzun metin buraya gelecek ve satır satır saracak.",
            text_size=(self.width, None),
            size_hint_y=None,
            height=100,
            halign='left',
            valign='top'
        )
        self.etiket.bind(size=lambda inst, val: setattr(inst, 'text_size', (inst.width, None)))
        self.add_widget(self.etiket)

    def update_text_size(self, instance, value):
        instance.text_size = (instance.width, None)

    def ekle(self, instance):
        hastalik = self.Hastalık.text
        islem = self.islem.text
        ilac = self.ilac.text

        self.etiket.text = f"Hastada alınan sözlü anamnezde {hastalik} geçmişi olduğu ilaç kullandığı kullandığı ilacın ismini {ilac} öğrenilmiştir. Hastaya {islem} uygulanacaktır. Tarafınızca değerlendirilmesi rica olunur."

class Konapp(App):

    def build(self):
        return generator()


if __name__ == '__main__':
    Konapp().run()