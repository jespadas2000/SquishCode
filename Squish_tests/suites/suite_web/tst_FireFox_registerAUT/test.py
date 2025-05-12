# -*- coding: utf-8 -*-

import Funtions.Funtions_Global as fg

def main():
    fg.regAppInServer(fg.TOOL_EXPLORER, fg.PROGRAM_PATH_EXPLORER, True)
    fg.regAttachableAppInServer(fg.TOOL_EXPLORER, "5050", True)
