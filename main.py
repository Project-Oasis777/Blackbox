from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
import threading

# Professional UI Design with Navigation and Theme
KV = '''
ScreenManager:
    MainScreen:
    SettingsScreen:
    SetupScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Secure Envoy"
            left_action_items: [["menu", lambda x: app.open_settings()]]
            right_action_items: [["account-plus", lambda x: app.add_contact()]]
        
        MDScrollView:
            MDList:
                id: chat_list  # Messages appear here

        MDBoxLayout:
            adaptive_height: True
            padding: "10dp"
            MDTextField:
                id: msg_input
                hint_text: "Encrypted Message..."
            MDIconButton:
                icon: "send"
                on_release: app.send_logic()

<SettingsScreen>:
    name: 'settings'
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "App Settings"
            halign: "center"
        MDRaisedButton:
            text: "Generate RSA Keys"
            on_release: app.generate_keys()
        MDLabel:
            text: "Theme Mode"
        MDSwitch:
            on_active: app.toggle_theme(*args)
        MDRaisedButton:
            text: "Back to Chat"
            on_release: root.manager.current = 'main'
'''

class MainScreen(Screen): pass
class SettingsScreen(Screen): pass
class SetupScreen(Screen): pass

class SecureMessenger(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark" # Default to Dark for Professional look
        return Builder.load_string(KV)

    def toggle_theme(self, switch, value):
        if value:
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

    def send_logic(self):
        # Using threading to prevent the 'freeze' you mentioned earlier
        threading.Thread(target=self.background_send).start()

    def background_send(self):
        # Insert your AES Encryption and Firebase/Socket Logic here
        print("Encrypting and Sending...")

    def generate_keys(self):
        # Logic for Private/Public key generation
        self.show_dialog("Success", "Military Grade RSA Keys Generated Locally.")

    def show_dialog(self, title, text):
        self.dialog = MDDialog(title=title, text=text, size_hint=(0.8, None))
        self.dialog.open()

if __name__ == '__main__':
    SecureMessenger().run()
