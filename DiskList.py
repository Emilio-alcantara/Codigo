import string,os,shutil
available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
total_discos = len(available_drives)
bucle = 0
while bucle < total_discos:
    print (available_drives[bucle])
    bucle = bucle + 1

#print (platform.system()) 




