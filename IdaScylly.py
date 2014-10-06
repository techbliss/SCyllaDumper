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
        idaapi.msg("Scylla Plugin is found. \n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")

    def AddMenuElements(self):
        idaapi.add_menu_item("Debugger/", "Scylla", "", 0, self.Dark, ())


    def run(self, arg=0):
        idaapi.msg("")

        self.AddMenuElements()


    def Dark(self):
        import os
        import sys
	if __EA64__:
		subprocess.Popen(os.path.join(os.path.expanduser('~'), os.path.expandvars('%IDADIR%'),
	'Scylla_x64.exe'), shell=True)
	
	else:
		subprocess.Popen(os.path.join(os.path.expanduser('~'), os.path.expandvars('%IDADIR%'),
	'Scylla_x86.exe'), shell=True)


def PLUGIN_ENTRY():
    return Pizza()