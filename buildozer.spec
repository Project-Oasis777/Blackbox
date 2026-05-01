[app]

title = Secure Envoy
package.name = secureenvoy
package.domain = org.wayne
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pem
version = 0.1

# Stable requirements - removed cryptography/openssl for now
requirements = python3,kivy==2.3.0,kivymd==2.0.1,requests,plyer,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,READ_CONTACTS,WRITE_CONTACTS,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,NEARBY_WIFI_DEVICES,SEND_SMS

android.archs = arm64-v8a,armeabi-v7a
android.api = 33
android.minapi = 21
android.accept_sdk_license = True
android.allow_backup = True

# Stability & build flags
p4a.branch = develop
log_level = 2
warn_on_root = 1
