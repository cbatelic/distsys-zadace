
def function(x,y):
    if type(x) is list and type(y) is dict:
        print('Parametri su lista i dictionary')
        if len(x) == len(y): print('Parametri imaju isti broj elemenata.')
        if set(map(type, x)) == {int}: print('Svi elementi u listi su int')
     
    else: print('Error: parametri nisu lista i dictionary.')
    
function([8,7,1], {1:2,2:1,3:2})
