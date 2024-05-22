import shutil, platform,os,string


so_name = platform.system()

if so_name == 'Windows' :
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    for letra in available_drives:
        total, used, free = shutil.disk_usage(letra)
        print("Disco", letra,"total %d GiB" % (total  // (2**30)))
        print("Disco", letra,"usado %d GiB" % (used  // (2**30)))
        print("Disco", letra,"libre %d GiB" % (free  // (2**30)))

else:
    print("No es Windows")

    shutil._ntuple_diskusage