import os

f = r'' #labels directory

for filename in os.listdir(f):
    if filename.endswith(".txt"):
        with open(filename, 'r+') as file:
            lines = file.readlines()
            file.seek(0, 0) #set the pointer to 0,0 cordinate of file
            for line in lines:
                row = line.strip().split(" ")
                if row[0] == '4':                    
                    row[0] = '1'
                    print(row)
                    file.write(" ".join(row) + "\n")