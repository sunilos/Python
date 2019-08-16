#Copy a Binary File
import shutil
source = "F:/baby.jpg";
target = "F:/boy.jpg";
shutil.copyfile(source,target)
print(source + " is copied to " + target)
