#!/usr/bin/env python3

#import directory
import shutil
import os

#run script from any where in directory
os.chdir('/home/student/mycode/')

#move files from DirectoryA to DirectoryB (will overwrite content)
shutil.move('raynor.obj', 'ceph_storage/')

#prompt user for new name of file
xname = input('What is the new name for kerrigan.obj? ')

#rename current object file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

