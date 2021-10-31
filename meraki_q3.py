##Q.3 Python object ko json string mai convert karne ka program likho?
import json
b={
    "name": "David", 
    "class": "I", 
    "age": 6,
    "pk":3009
}

a=json.dumps(b)
print(a)