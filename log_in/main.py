from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
import pyrebase


Window.size = (480, 700)

class LoginInterface(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        firebase_config= {
            'apiKey': "AIzaSyB023tSuxt0R-5DEmmxiF_A2iN7mdLdPvM",
            'authDomain': "kivymd-7f027.firebaseapp.com",
            'databaseURL': "https://kivymd-7f027-default-rtdb.firebaseio.com",
            'projectId': "kivymd-7f027",
            'storageBucket': "kivymd-7f027.appspot.com",
            'messagingSenderId': "316772671836",
            'appId': "1:316772671836:web:0ed54bb6dcf614b685a199",
            'measurementId': "G-0D1B8JW0J5"
        }
        firebase = pyrebase.initialize_app(firebase_config)
        self.db = firebase.database()
        #data = {'Email': 'xyz@gmail.com', 'Password': '12345'}
        #db.child('CustomKey1').set(data)
        #data1 = {'Email': 'abc@gmail.com', 'Password': '12345'}
        #db.child('CustomKey2').set(data1)

        #Reading Database
        #database_data=db.get()
        #for s_d in database_data.each():
            #print(s_d.val())



    def creator(self):
        cond = True

        username = self.ids.username.text
        email = self.ids.signup_email.text
        password = self.ids.signup_password.text
        # Loop through to ensure the username has not being used by amother user
        if username != '' and email != '' and password != '':
            dd = self.db.get()
            if dd.val()==None:
                data = {'Username': username, 'Email': email, 'password': password}
                self.db.child(username).set(data)
                print('Signup Success')

            else:
                for sd in dd.each():
                    dict = sd.val()
                    if dict['Username']== username or dict['Email'] == email:
                        cond=False
                        print('Sign Up Failed ')
                        dialog = MDDialog(title='SignUp Information', text='SignUp Failed')
                        dialog.open()
                        break

            if cond== True:
                data = {'Username': username, 'Email': email, 'password': password}
                self.db.child(username).set(data)
                print('Login Success')
                dialog = MDDialog(title='SignUp Information', text='SignUp Success')
                dialog.open()

        else:
            dialog = MDDialog(title='SignUp Information', text='Please Fill this fields')
            dialog.open()
    def login(self):
        cond = False
        email = self.ids.login_email.text
        password = self.ids.login_password.text
        # First check and ensure the database is not empty
        # Check my database if this email is available if it is print a success message else fail
        db = self.db.get()
        if db.val()!= None:
            for s_d in db.each():
                dict = s_d.val()
                if dict['Email']==email and dict['password']==password:
                    print('Login Success')
                    dialog=MDDialog(title='Login Information', text='Login Success')
                    dialog.open()
                    cond=True
                    break

            if cond==False:
                print('Login Failed')
                dialog = MDDialog(title='Login Information', text='Login Failed')
                dialog.open()

        else:
            print('Login Failed')



class LoginApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette='Yellow'
        self.theme_cls.theme_style='Dark'

    def color_changer(self):
        if self.theme_cls.theme_style=='Dark':
            self.theme_cls.theme_style= 'Light'
            self.theme_cls.primary_palette= 'DeepPurple'

        else:
            self.theme_cls.primary_palette = 'Yellow'
            self.theme_cls.theme_style = 'Dark'



LoginApp().run()