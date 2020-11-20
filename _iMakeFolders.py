import shutil
import os

#ENTER FOLDER NAME HERE##################################################
FolderName = input("A name, a name, give me a name, short and auspicious and not quite the same as anything older that sits in the same folder : ")
#FolderName    = 'And there shall in that time be rumours of things going astray'
#########################################################################


l             = []
src           = 'R:/RP&D/SAM/PRA/_Resources/_Folder Convention'
dst           = 'R:/RP&D/SAM/PRA/_Projects/Active/'
numdir        = 1

def copytree(src, dst, symlinks=False, ignore=None):
    
    path    = dst + FolderName
    l.append(str(path))
    
    for item in l:
        os.mkdir(str(item))

    for i in l:    
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(i, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
            
copytree(src, dst)


print("Your folder has been created here: "+dst + FolderName)

print("")

print('"...there will be a great confusion as to where things really are...<Life of Brian>"')

print('Press Enter to exit')
