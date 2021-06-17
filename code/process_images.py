import os, glob

def add_prefix(directory, prefix):
    files = glob.glob("%s/*.*" % directory)
    for file in files:
        name = file.split("/")[-1]
        if not name.startswith(prefix):
            new_name = "%s%s" % (prefix, name)
            os.rename(file, "%s/%s" % (directory, new_name))

def process_images(directory):
    files = glob.glob("%s/roh/*.*" % directory)
    for file in files:
        if not file.endswith(".jpg"):
            ending = file.split(".")[-1]
            newname = file.replace(".%s"%ending, ".jpg")
            os.system('convert "%s" "%s"' % (file, newname))
            if os.path.exists(newname):
                os.system('rm "%s"' % file)
                file = newname
            else:
                print("FAILED TO CONVERT %s" % file)
        target = "%s/fertig/%s.png" % (directory, file.split("/")[-1].split(".")[0])
        if not os.path.exists(target):
            cmd = 'magick "%s"  -fuzz 1%% -fill none -draw "alpha 1,1 floodfill" -trim +repage -resize 1000x1000\>  "%s" ' % (file, target)
            os.system(cmd)

process_images("Inventar")
process_images("BilderVerbrauchsmaterial")
#add_prefix("Inventar/roh/", "I")