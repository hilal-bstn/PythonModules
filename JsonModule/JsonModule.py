import json
person_string='{"name":"Ali","languages":["python","C#"]}'
#result=json.loads(person_string)#person_string i dictionary e çevirir.
#result=result["name"]

with open("person.json") as f:#person.json dosyası içindeki yazıları yazdırdık
    data=json.load(f)
    print(data["name"])


person_dict={"name":"Ali","language":["Python","c#"]}
result=json.dumps(person_dict)#stringe çevirdik sözlüğü(dictionary to string)
print(result)
print(type(result))

with open("person_json","w") as f:
    json.dump(person_dict,f)#dosyaya ekleme yapıyoruz

