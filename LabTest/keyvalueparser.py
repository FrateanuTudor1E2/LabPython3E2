import re

def read_from_ini_file(filepath):
 try:
  for line in open(filepath):
     print (line.strip())
 except IOError:
  print ("[ERROR] - I/O error")

read_from_ini_file("C:\\Users\\tudor\\PycharmProjects\\LabPython3E2\\LabTest\\in.ini")



