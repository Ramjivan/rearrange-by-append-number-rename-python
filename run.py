import os 

DIR = "C:/Users/ramji/Desktop/B/"

FILES_ARR = os.listdir(DIR)
MOVE_TO_LAST = []
NUMBERS_LIST = []
countf = open("countf.txt", "w+")
COUNT = int(input("Enter starting index"))
while COUNT < int(len(FILES_ARR)):
    filename = FILES_ARR[COUNT]
    print(filename + ' ')
    value = input("")
    if value == "x":
        #delete file
        os.remove(DIR+filename)
        COUNT = COUNT + 1
        fw = open("countf.txt", "w")
        fw.write(str(COUNT))
        fw.close()
    elif value == "":
        #move file to be renamed in last
        MOVE_TO_LAST.append(filename)
        COUNT = COUNT + 1
        fw = open("countf.txt", "w")
        fw.write(str(COUNT))
        fw.close()
    else:
        newname = DIR+ str(value).zfill(3) + ' ' + filename
        os.rename(DIR + filename,  newname)
        NUMBERS_LIST.append(value)
        COUNT = COUNT + 1
        fw = open("countf.txt", "w")
        fw.write(str(COUNT))
        fw.close()




        
    



