import json

dic1={"Name":"Ram","Class":"IV", "Age":9}
text_file=open("myfile.json","w")
json.dump(dic1,text_file)
text_file.close()
# print(text_file)


text_file=open("myfile.json","r")
a=json.load(text_file)
text_file.close()
print(a)