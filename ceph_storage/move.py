#!/usr/bin/env python3
###Testing a move file""

import shutil
import os

def main():

   os.chdir('/home/student/mycode/') #directory where file resides
   shutil.move ('moveplease01.py', 'ceph_storage/') #destination of moved file

main()
