import json
import pprint

def studenti(tuple, key):
    newListDict= []
    for x in tuple:
        newListDict.append(dict(zip(key,x)))
        pprint.pprint(sorted(newListDict, key=lambda x: x['id']))
        print(newListDict)
        
studenti([(121,'Ivan','Ivic'),(431,'Pero','Horvat'),(31,'Marija','Maric')],['id', 'ime', 'prezime'] )
