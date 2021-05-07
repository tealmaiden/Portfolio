import time
import shutil
import os


class main():
     

    def moveUpdatedFiles():
        src = (os.getcwd()+'\\')
        dst = ('C:\Python27\\techAcademy\\Drills\\drillP67-Destination\\')
        print 'Source folder:', src
        print 'Destination folder:', dst
        count = 0   #num files moved
        a = ('\n*************************( Check Complete )*************************')  #new line w/ string 
        b = ('********************************************************************')
        for f in os.listdir(src):
            if f.endswith(".txt"):
                srcPath = (os.path.join(src, f))    #path = source + file
                dstPath = (os.path.join(dst, f))
                mtime = (os.path.getmtime(srcPath)) #seconds from the epoch when file was modified
                now = time.time()                   #seconds from the epoch currently
                diff = now - mtime
                if diff <= 86400:                   #move if mod happened < 86400s ago
                    shutil.move(srcPath, dstPath)   #add source dir to filename
                    print 'Change made to',f,'within 24 hr. File moved from Source to Destination folder.'
                    count = count + 1 
        if (count > 1):
            print(a)
            print("{} files have been moved into the destination directory".format(count))
            print(b)
        elif (count == 1):
            print(a)
            print("1 file has been moved into the destination directory") #file singular
            print(b)
        else:
            print(a)
            print("No files need to be moved at this time.")
            print(b)

    moveUpdatedFiles()


if __name__ == '__main__':
    main()

            
