import subprocess
import idaapi
import idc
from idc import *
from idaapi import *
import os
import sys


class Pizza(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "This is a comment"

    help = "Scylla"
    wanted_name = "Scylla"
    wanted_hotkey = "Alt-F7"

    def init(self):
        idaapi.msg("\n Scylla Plugin is found. \n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")

    def AddMenuElements(self):
        idaapi.add_menu_item("View/", "Scylla", "", 0, self.Dark, ())


    def run(self, arg=0):
        idaapi.msg("")

        self.AddMenuElements()


    def Dark(self):
        g = globals()
        idahome = idaapi.idadir("plugins\\scylla")
        if __EA64__:
            subprocess.Popen(idahome + '\\Scylla_x64.exe')
    
        else:
            g = globals()
            idahome = idaapi.idadir("plugins\\scylla")

            subprocess.Popen(idahome + '\\Scylla_x86.exe')

def PLUGIN_ENTRY():
    return Pizza()