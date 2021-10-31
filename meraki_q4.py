## Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

import json
kapil={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
    
dic1={'4': 5,'6': 7,'1': 3,'2': 4}

with open("Sortdic.json","w") as f:
    json.dump(dic1,f,sort_keys=True)
