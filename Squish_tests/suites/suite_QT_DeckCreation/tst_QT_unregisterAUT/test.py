# -*- coding: utf-8 -*-
import Funtions.Funtions_Global as fg

def main():
     fg.regAppInServer(fg.TOOL_Ecosimpro, fg.PROGRAM_PATH_ECOSIMPRO, False)
     fg.regAttachableAppInServer(fg.TOOL_Ecosimpro, "5050", False)