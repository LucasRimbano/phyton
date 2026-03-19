import pandas as pd    

alumnos = {
      "nombre": ["lucas" , "maria" , "juan" , "david" , "gonzalo" , "candela"] ,
       "materia" : ["matematica", "matematica" ,"informatica" ,"informatica" ,"matematica" ,"informatica"] ,
       "nota" : [8,6,5,9,5,9] 
} 


print(alumnos)

df = pd.DataFrame(alumnos)
print(df)

print("Promedio de nota general:" ,df["nota"].mean())
print("Aprobados",df[df["nota"]>7])
