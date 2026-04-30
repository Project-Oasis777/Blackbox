[app]
title = My Secure Messenger
package.name = securemessenger
package.domain = org.wayne
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy, kivymd, pycryptodome, requests, plyer
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0 
android.permissions = INTERNET, READ_CONTACTS, WRITE_CONTACTS, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_FINE_LOCATION, NEARBY_WIFI_DEVICES
android.archs = arm64-v8a
android.allow_backup = True
[buildozer]
log_level = 2
warn_on_root = 1
