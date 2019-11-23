import pandas as pd
cars = pd.read_csv('cars.csv')
#1:1st 5 rows with odd numbered columns
cars5 = cars.iloc[[0,1,2,3,4],[1,3,5,7,9,11]]
print('\n#1:The first 5 rows with odd-numbered columns: \n',cars5)
#2:Row that contains 'model' of 'Mazda RX4'
rx4 = cars.loc[cars['Model']=='Mazda RX4',:]
print('\n#2:The row that contains Mazda RX4: \n',rx4)
#3:Cyl that Camaro Z28 have
Camaro_cyl = cars.loc[cars['Model']=='Camaro Z28','cyl']
print('\n#3:The number of cylinders the Camaro Z28 has: \n',Camaro_cyl)
#4: # of cylinders and gear type of the models 'Mazda RX4 Wag', 'Ford Pantera L','Honda Civic',
cylgear = cars.loc[(cars['Model']=='Mazda RX4 Wag')|(cars['Model']=='Ford Pantera L')|
        (cars['Model']=='Honda Civic'),['Model','cyl','gear']]
print('\n#4:The number of cylinders and the gear type of models:Mazda RX4 Wag,Ford Pantera L,Honda Civic \n',cylgear)
      