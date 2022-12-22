import sqlite3

# Connect to the database
conn = sqlite3.connect('Locations.db')

# Create a cursor
cursor = conn.cursor()

# Create a table
#cursor.execute('''CREATE TABLE Location (id INTEGER PRIMARY KEY, name TEXT,lat FLOAT, long FLOAT)''')


running=True
while running:
    entry_name = input("Enter name of Location: ")
    if entry_name == 'exit':
        break
    lat=input("latitude: ")
    long=input("longitude: ")
    cursor.execute(f"INSERT INTO Location (name, lat, long ) VALUES ('{entry_name}', '{lat}', '{long}')")
conn.commit()

# Close the connection
conn.close()