import sqlite3

# Connect to the database
conn = sqlite3.connect('Locations.db')

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE Location (id INTEGER PRIMARY KEY, name TEXT,long FLOAT, lat FLOAT)''')


with open("locations_txt.txt",'r',encoding='utf-8') as text_file:
    text_file = text_file.readlines()
    for line in range(1,len(text_file)):
        text_line = text_file[line].split(';')
        text_line[2]=text_line[2].strip('\n')
        name,lat,long=text_line
        print("hello")
        cursor.execute(f"INSERT INTO Location (name, lat, long ) VALUES ('{name}', '{lat}', '{long}')")
conn.commit()

# Close the connection
conn.close()

