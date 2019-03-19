inp = "-project/--file.txt/--folder2/---file2.txt/---folder21/----file21.txt/---folder22/----file22.txt"
ar = inp.split("/")

x=0
path = {}
files = {}
path3 = []
fullpath = []
while True:
    try:
        item = ar[x]
        print(item)
        ind = item.count("-")
        print(ind)
        
        name = item[ind:]

        try:
            ext = name.split(".")
            print(ext[1])

            jep = ind - 1
            y = 1
            fp = ""
            for key, value in path.items():
                if key <= jep:
                    fp += value + "/"
                if key == jep:
                    fp += name
                    path3.append(fp)
                
            
        except Exception:
            path[ind] = name
            #print(path)
            pass
        x+=1
    except IndexError:
        break
print(path3)

