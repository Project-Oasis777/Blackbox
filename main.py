import threading
import os
import webbrowser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import StringProperty, ColorProperty # Added these
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from plyer import share

# For encryption
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# ====================== KV Language ======================
KV = '''
ScreenManager:
    MainScreen:
    SettingsScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Secure Envoy"
            left_action_items: [["menu", lambda x: app.root.current = 'settings']]
        
        MDScrollView:
            id: scroll_view
            MDList:
                id: chat_list
                padding: "10dp"
                spacing: "12dp"

        MDBoxLayout:
            adaptive_height: True
            padding: "8dp"
            spacing: "8dp"
            MDTextField:
                id: msg_input
                hint_text: "Type encrypted message..."
                mode: "rectangle"
            MDIconButton:
                icon: "send"
                on_release: app.send_message()

<ChatBubble>:
    size_hint: None, None
    # FIXED: Removed quotes around self.minimum_height
    size: "280dp", self.minimum_height
    padding: "12dp"
    radius: [15, 15, 15, 15]
    md_bg_color: root.bubble_color

    MDLabel:
        text: root.message_text
        adaptive_height: True
        theme_text_color: "Custom"
        text_color: root.text_color
        markup: True

<SettingsScreen>:
    name: 'settings'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Security"
            left_action_items: [["arrow-left", lambda x: app.root.current = 'main']]
        MDScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                adaptive_height: True
                padding: "20dp"
                spacing: "20dp"
                MDRaisedButton:
                    text: "Generate RSA Keys"
                    pos_hint: {"center_x": .5}
                    on_release: app.generate_keys()
                MDLabel:
                    text: "Theme Mode"
                    halign: "center"
                MDSwitch:
                    pos_hint: {"center_x": .5}
                    on_active: app.toggle_theme(self, self.active)
'''

class MainScreen(Screen): pass
class SettingsScreen(Screen): pass

class ChatBubble(MDCard):
    # FIXED: Use Kivy Properties so the UI updates correctly
    message_text = StringProperty("")
    bubble_color = ColorProperty([0.2, 0.6, 1, 1])
    text_color = ColorProperty([1, 1, 1, 1])

class SecureMessenger(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def toggle_theme(self, switch, value):
        self.theme_cls.theme_style = "Light" if value else "Dark"

    def generate_keys(self, silent=False):
        def _task():
            try:
                private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
                # Key saving logic here...
                Clock.schedule_once(lambda dt: self.show_dialog("Success", "4096-bit Keys Generated"))
            except Exception as e:
                Clock.schedule_once(lambda dt: self.show_dialog("Error", str(e)))
        
        threading.Thread(target=_task).start()

    def add_chat_bubble(self, message: str, is_sent: bool = True):
        chat_list = self.root.get_screen('main').ids.chat_list
        bubble = ChatBubble()
        bubble.message_text = f"[b]You[/b]\\n{message}" if is_sent else f"[b]Friend[/b]\\n{message}"
        bubble.pos_hint = {"right": 1} if is_sent else {"left": 1}
        chat_list.add_widget(bubble)

    def send_message(self):
        screen = self.root.get_screen('main')
        msg = screen.ids.msg_input.text
        if msg:
            self.add_chat_bubble(msg)
            screen.ids.msg_input.text = ""

    def show_dialog(self, title, text):
        MDDialog(title=title, text=text, size_hint=(0.8, None)).open()

    def invite_friend(self, platform):
        msg = "Join Secure Envoy!"
        if platform == "share_sheet":
            share.share(title="Invite", text=msg)
        else:
            webbrowser.open(f"sms:?body={msg}")

if __name__ == '__main__':
    SecureMessenger().run()
