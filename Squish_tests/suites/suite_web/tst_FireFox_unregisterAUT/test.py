import Funtions.Funtions_Global as fg

def main():
    fg.regAppInServer(fg.TOOL_FIREFOX, fg.PROGRAM_PATH_FIREFOX, False)
    fg.regAttachableAppInServer(fg.TOOL_FIREFOX, "5050", False)