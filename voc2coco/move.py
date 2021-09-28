import shutil 


train = []
with open("train.txt", "r") as file:
    lines = file.readlines()
    #print(lines)
    for line in lines:
        line = line.strip()
        train = train + [line+'.jpg']

src = './JPEGImages/' 
dir = './train/' 

for i in train:

    filename = i 
    shutil.move(src + filename, dir + filename)


####################################

val = []
with open("val.txt", "r") as file:
    lines = file.readlines()
    #print(lines)
    for line in lines:
        line = line.strip()
        val = val + [line+'.jpg']

src = './JPEGImages/' 
dir = './val/' 

for i in val:

    filename = i 
    shutil.move(src + filename, dir + filename)




