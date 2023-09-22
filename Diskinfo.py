import shutil, platform


so_name = platform.system()

if so_name == 'Windows' :
    total, used, free = shutil.disk_usage("c:")
    print("Total: %d GiB" % (total  // (2**30)))
else:
    print("No es Windows")

    shutil._ntuple_diskusage