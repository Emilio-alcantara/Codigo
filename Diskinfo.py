import shutil

total, used, free = shutil.disk_usage("c:")

print("Total: %d GiB" % (total  // (2**30)))




