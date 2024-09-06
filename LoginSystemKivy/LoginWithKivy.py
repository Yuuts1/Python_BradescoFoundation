from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Criação dos widgets
        self.username_label = Label(text='Nome de usuário:')
        self.username_input = TextInput(multiline=False)
        
        self.password_label = Label(text='Senha:')
        self.password_input = TextInput(password=True, multiline=False)
        
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.verify_login)
        
        # Adiciona os widgets ao layout
        self.add_widget(self.username_label)
        self.add_widget(self.username_input)
        self.add_widget(self.password_label)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)

    def verify_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        # Verifica credenciais simples (apenas um exemplo)
        if username == "usuario" and password == "senha123":
            self.show_popup("Sucesso!", "Login bem-sucedido!")
        else:
            self.show_popup("Falha!", "Nome de usuário ou senha incorretos.")
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message),
                      size_hint=(None, None), size=(300, 200))
        popup.open()

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
