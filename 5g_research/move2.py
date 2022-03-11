#!/usr/bin/env python3

###Moving files into 5g_research to clean up directory###

import shutil 
import os #two lines required to move/files

def main():
    
    os.chdir('/home/student/mycode/') #directory where file resides
    shutil.move('5g_research_backup', '5g_research/') #new destination

main()

