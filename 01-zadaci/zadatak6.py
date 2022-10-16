
def mergedList(x,y):
   if type(x) == type(y):
       print('Parametri su istog tipa!')
       if type(x)and type(y) is list or dict: 
           print('Parametri su lista ili dictionary.')
       if type(x and y) is list:
           print('Parametri su: lista.')
           mergedList= x + y
           print(mergedList)
       elif type(x and y) is dict:
           print('Parametri su: dictionary.')
           mergedDict= x.copy()
           mergedDict.update(y)
           print(mergedDict)     
       else: print('Error: Parametri nisu lista ili dictionary.')
   else:print('Error: parametri nisu isti!!')
        
          
mergedList([1,2,1,2],[3,2])
