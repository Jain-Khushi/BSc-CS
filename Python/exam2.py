try:
    file1 = open("file1.txt")
    file2 = open("file2.txt", "w+")

    words = []

    for row in file1:
        words.extend(row.split())
        
    for word in words:
        vcount = 0
        for i in word:
            if i.lower() in "aeiou":
                vcount += 1;
        file2.write(word+"?"+str(len(word))+"?"+str(vcount)+"\n")

    file1.close()
    file2.close()
    
    f2 = open("file2.txt")
    
    for r in f2.readlines():
        print(r)
    
    f2.close()

except FileNotFoundError:
    print("file 1 does not exists")
