[app]
title = Secure Envoy
package.name = secureenvoy
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# CRITICAL: Requirements must include cryptography and its backends
requirements = python3, kivy==2.3.0, kivymd==1.2.0, pillow, cryptography, pyopenssl, plyer

orientation = portrait

# Android specific
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Ensure the cryptography recipe is used correctly
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
