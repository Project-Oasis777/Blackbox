import os
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty, ColorProperty
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager, Screen

# Handle Cryptography safely
try:
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
except ImportError:
    print("Cryptography not found. Ensure it is in buildozer.spec")

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
            left_action_items: [["menu", lambda x: app.open_settings()]]
            elevation: 4
        
        MDScrollView:
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
                hint_text: "Type message..."
                mode: "rectangle"
            MDIconButton:
                icon: "send"
                on_release: app.send_message()

<SettingsScreen>:
    name: 'settings'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Settings"
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
        MDLabel:
            text: "Encryption Settings"
            halign: "center"

<ChatBubble>:
    size_hint: None, None
    size: "280dp", self.minimum_height
    padding: "12dp"
    radius: [15, 15, 15, 15]
    md_bg_color: self.bubble_color

    MDLabel:
        text: root.message_text
        adaptive_height: True
        theme_text_color: "Custom"
        text_color: root.text_color
'''

class ChatBubble(MDCard):
    message_text = StringProperty("")
    bubble_color = ColorProperty([0.9, 0.9, 0.9, 1])
    text_color = ColorProperty([0, 0, 0, 1])

class MainScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class SecureEnvoyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

    def send_message(self):
        text = self.root.get_screen('main').ids.msg_input.text
        if text:
            chat_list = self.root.get_screen('main').ids.chat_list
            bubble = ChatBubble(
                message_text=text,
                bubble_color=self.theme_cls.primary_color,
                text_color=[1, 1, 1, 1]
            )
            chat_list.add_widget(bubble)
            self.root.get_screen('main').ids.msg_input.text = ""

    def open_settings(self):
        self.root.current = 'settings'

    def go_back(self):
        self.root.current = 'main'

if __name__ == '__main__':
    SecureEnvoyApp().run()
