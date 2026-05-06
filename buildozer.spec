[app]
title = MonsterRun
package.name = monsterrun
package.domain = org.ilyas
source.dir =.
source.include_exts = py
version = 0.1
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
