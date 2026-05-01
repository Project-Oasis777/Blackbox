[app]
title = Secure Envoy
package.name = secureenvoy
package.domain = org.wayne
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pem
version = 0.1

# FIXED: Pinned KivyMD version and added pyjnius for hardware access
requirements = python3, kivy==2.3.0, kivymd==1.2.0, cryptography, openssl, pyjnius, requests, urllib3, chardet, idna, certifi, plyer

orientation = portrait
fullscreen = 0 

# Permissions look good for your A50 and nearby device features
android.permissions = INTERNET, READ_CONTACTS, WRITE_CONTACTS, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, NEARBY_WIFI_DEVICES, SEND_SMS

# Dual architecture is the right move for Samsung stability
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
