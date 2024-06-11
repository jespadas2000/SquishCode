# -*- coding: utf-8 -*-
import Funtions.Funtions_Global as fg

def main():
     fg.regAppInServer(fg.TOOL_NAME, fg.PROGRAM_PATH_INSTALL, True)
     fg.regAttachableAppInServer(fg.TOOL_NAME, "5050", True)