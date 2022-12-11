from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivymd.app import MDApp
from textblob import TextBlob

Window.size= (480, 800)

class MainInterface(RelativeLayout):

    def cleaner(self):
        self.ids.input.text = ''

    def submitter(self):
        blob = TextBlob(self.ids.input.text)

        st = blob.sentences

        print(st)


class TextAnalyzerApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette= 'Green'
        self.theme_cls.theme_style= 'Dark'
        return 0

TextAnalyzerApp().run()