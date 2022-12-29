with open("locations_txt.txt",'r',encoding='utf-8') as text_file:
    text_file = text_file.readlines()
    for line in range(1,len(text_file)):
        text_line = text_file[line].split(';')
        text_line[2]=text_line[2].strip('\n')
        name,lat,long=text_line
        print("hello")
