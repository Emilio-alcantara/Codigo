import psutil
#available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
#print (available_drives)

#print (platform.system()) 

drives = psutil.disk_partitions()

print (drives)
