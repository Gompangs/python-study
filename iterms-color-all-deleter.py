# -*- coding: utf-8 -*-

import os


def copy_file():
    os.system("cp ~/Library/Preferences/com.googlecode.iterm2.plist .")
    os.system("plutil -convert xml1 com.googlecode.iterm2.plist")


def process():
    file = open("com.googlecode.iterm2.plist", 'r')
    lines = file.readlines()

    # remove custom color presets
    start = 0
    end = 0
    cnt = 0
    for line in lines:
        if "Custom Color Presets" in line:
            # remove below attribute
            start = cnt
        if "Default Bookmark Guid" in line:
            print(line)
            end = cnt
        cnt = cnt + 1

    cnt = 0
    isTarget = False
    file = open("com.googlecode.iterm2.plist", 'w')
    for line in lines:
        if cnt == start:
            isTarget = True
        if cnt == end:
            isTarget = False

        if not isTarget:
            file.write(line)
        cnt = cnt + 1

    file.close()
    overwrite_plist()


def overwrite_plist():
    os.system("cp com.googlecode.iterm2.plist ~/Library/Preferences/")
    os.system("defaults read ~/Library/Preferences/com.googlecode.iterm2")


copy_file()
process()
