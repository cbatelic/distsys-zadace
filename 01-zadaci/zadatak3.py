def articles(x):
    if type(x) is list: print('Parametar je lista.')
    if all(isinstance(i, dict) for i in x):print('Svi elementi su dictionary.')
    elif all(('cijena','naziv', 'kolicina') in keys for keys in x):print('Svi elemnti imju 3 kljuca.')
    count={'ukupno':{ 'artikli' : [x[0]['naziv'], x[1]['naziv'], x[2]['naziv']],'cijena': x[0]['cijena']+(x[1]['cijena']*2)+x[2]['cijena']}}
    print(count)
    
    
articles([{'cijena':8,'naziv':'Kruh','kolicina':1}, {'cijena':13,'naziv':'Sok','kolicina':2},
{'cijena':7,'naziv':'Upaljac','kolicina':1}])

