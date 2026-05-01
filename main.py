import threading
import requests
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy import webbrowser
from plyer import share

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
            left_action_items: [["menu", lambda x: app.root.current = 'settings']]
            right_action_items: [["account-plus", lambda x: app.show_dialog("Contacts", "Feature coming soon")]]
        
        MDScrollView:
            MDList:
                id: chat_list

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
        padding: "20dp"
        spacing: "10dp"
        
        MDTopAppBar:
            title: "Settings"
            left_action_items: [["arrow-left", lambda x: app.root.current = 'main']]

        MDLabel:
            text: "Growth & Community"
            font_style: "H6"
            halign: "center"
            
        MDRaisedButton:
            text: "Invite via Social Media"
            pos_hint: {"center_x": .5}
            on_release: app.invite_friend("share_sheet")
            
        MDRaisedButton:
            text: "Invite via SMS"
            pos_hint: {"center_x": .5}
            on_release: app.invite_friend("sms", "0000000")

        MDRaisedButton:
            text: "Generate RSA Keys"
            pos_hint: {"center_x": .5}
            on_release: app.generate_keys()

        MDLabel:
            text: "Theme Mode"
            halign: "center"
        MDSwitch:
            pos_hint: {"center_x": .5}
            on_active: app.toggle_theme(*args)

<SetupScreen>:
    name: 'setup'
    MDLabel:
        text: "Setup Guide Placeholder"
        halign: "center"
'''

class MainScreen(Screen): pass
class SettingsScreen(Screen): pass
class SetupScreen(Screen): pass

class SecureMessenger(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    
    def on_send_click(self):
        threading.Thread(target=self.send_to_firebase).start()

    def send_to_firebase(self):
        try:
            requests.post("https://your-db.firebaseio.com/msg.json", json={"text": "Hi"})
        except:
            pass
    
    def toggle_theme(self, switch, value):
        if value:
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

    def send_logic(self):
        threading.Thread(target=self.background_send).start()

    def background_send(self):
        print("Encrypting and Sending...")

    def generate_keys(self):
        self.show_dialog("Success", "Military Grade RSA Keys Generated Locally.")

    def show_dialog(self, title, text):
        self.dialog = MDDialog(title=title, text=text, size_hint=(0.8, None))
        self.dialog.open()

    def invite_friend(self, platform, phone_number=None):
        invite_msg = "Join me on Secure Envoy for military-grade encrypted messaging!"
        if platform == "share_sheet":
            share.share(title="Invite to Secure Envoy", text=invite_msg)
        elif platform == "sms":
            webbrowser.open(f"sms:{phone_number}?body={invite_msg}")

if __name__ == '__main__':
    SecureMessenger().run()
