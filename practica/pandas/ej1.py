import pandas as pd 

data = { 
    "peliculas" : ["A", "B" , "C" , "D"] ,
    "año" :       [2020,1996,2015,2025] ,
    "rating" :    [8.5 , 7.2 ,6.8,9.0] , 
    "genero" :    ["Accion" , "Drama" ,"Accion","Comedia"]

}

df =pd.DataFrame(data)
print(df)
print("Promedio de rating:", df["rating"].mean())
print("Cantidad por género:")
print(df["genero"].value_counts())