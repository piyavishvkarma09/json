## Q.2 Python object ko json data main convert karne ka program likho? 

import json
b={
    "name": "David", 
    "class": "I", 
    "age": 6
}

text=open("question2.json","w")
json.dump(b,text)
text.close()
