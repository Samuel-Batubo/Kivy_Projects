from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.image import Image as Image_Reader
from plyer import filechooser
from PIL import Image, ImageFilter
from io import BytesIO


Window.size=(1000, 600)

class Interface(MDBoxLayout):


    def select(self, location):
        loct = str(location[0])+"\\Image.jpg"
        self.img_effect.save(loct)


    def exporting(self):
        filechooser.choose_dir(title='Select a Folder', on_selection=self.select)


    def file_opener(self):
        self.raw_img = filechooser.open_file(title='Choose Your Image', filters=[('*.png', '*.jpg', '*.jpeg')])
        self.editable_img = Image.open(self.raw_img[0])
        self.ids.img_placeholder.source=self.raw_img[0]
        self.ids.width.text=str(self.editable_img.width)
        self.ids.height.text=str(self.editable_img.height)
        self.ids.rotate.text='0'

    def editor(self):
        # Resizing Image
        resized_img= self.editable_img.resize((int(self.ids.width.text), int(self.ids.height.text)))

        #Rotation
        rototed_img = resized_img.rotate(int(self.ids.rotate.text))


        #Effect
        if self.ids.blur.active:
            self.img_effect = rototed_img.filter(ImageFilter.BLUR)

        elif self.ids.contour.active:
            self.img_effect = rototed_img.filter(ImageFilter.CONTOUR)

        elif self.ids.detail.active:
            self.img_effect = rototed_img.filter(ImageFilter.DETAIL)

        elif self.ids.find_edges.active:
            self.img_effect = rototed_img.filter(ImageFilter.FIND_EDGES)

        else:
            self.img_effect= rototed_img



        # Displaying on PlaceHolder
        data = BytesIO()
        self.img_effect.save(data, format='png')
        data.seek(0)
        bytesIO =BytesIO(data.read())
        img = Image_Reader(bytesIO, ext='png')
        self.ids.img_placeholder.texture= img.texture


class Image_EditorApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette='Purple'
        self.theme_cls.theme_style='Dark'


Image_EditorApp().run()