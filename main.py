import socket
import threading
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from Crypto.Cipher import AES
import base64

# --- CONFIGURATION ---
# Replace with your Firebase URL from the console
FB_URL = "https://blackbox-9415e-default-rtdb.firebaseio.com/"
PORT = 5555

def encrypt_msg(text, key):
    key = key.ljust(32)[:32].encode('utf-8')
    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    return base64.b64encode(nonce + tag + ciphertext).decode('utf-8')

class SecureApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10)
        self.key_in = TextInput(hint_text="Key", password=True, size_hint_y=None, height=100)
        self.display = Label(text="Welcome to Secure Chat")
        self.msg_in = TextInput(hint_text="Message...")
        
        send_btn = Button(text="SEND (Cloud/Local)", size_hint_y=None, height=100)
        send_btn.bind(on_press=self.send_data)
        
        self.root.add_widget(self.key_in)
        self.root.add_widget(self.display)
        self.root.add_widget(self.msg_in)
        self.root.add_widget(send_btn)

        # Start offline listener thread
        threading.Thread(target=self.offline_listener, daemon=True).start()
        return self.root

    def send_data(self, instance):
        if not self.key_in.text: return
        enc = encrypt_msg(self.msg_in.text, self.key_in.text)
        
        # 1. Cloud (Firebase)
        try: requests.post(FB_URL, json={"m": enc})
        except: pass
        
        # 2. Local (Hotspot) - Attempts to send to standard Android hotspot IP
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("192.168.43.1", PORT)) # Default Hotspot IP
            s.send(enc.encode())
            s.close()
        except: pass
        
        self.msg_in.text = ""

    def offline_listener(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', PORT))
        s.listen(5)
        while True:
            conn, addr = s.accept()
            data = conn.recv(1024).decode()
            Clock.schedule_once(lambda dt: self.update_ui(data))

    def update_ui(self, data):
        self.display.text = f"New Encrypted Msg: {data[:20]}..."

if __name__ == "__main__":
    SecureApp().run()
