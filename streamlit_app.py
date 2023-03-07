import pandas as pd
import streamlit as st
import pickle
dfCalificaciones = pd.read_excel("tareas.xlsx")

dfCalificaciones["promedio"] = ( dfCalificaciones["tarea1"] + dfCalificaciones["tarea2"] +
                                dfCalificaciones["tarea3"] + dfCalificaciones["tarea4"]) / 4
                                
dfCalificaciones["final"] = dfCalificaciones["promedio"].apply(lambda x: "Aprobado" if x >= 70 else "Reprobado")

dfResultados = dfCalificaciones[ ["matricula","promedio","final"] ]

dfResultados

st.dataframe(dfResultados)

model = pickle.load(open("model.pkl","rb"))

data = {
        "age": 17,
        "job": "unemployed",
        "marital": "single",
        "education": "university.degree",
        "default": "no",
        "housing": "yes",
        "loan": "no",
        "contact": "cellular",
        "month": "may",
        "duration": 3000,
        "campaign": 50,
        "pdays": 500,
        "previous": 2000,
        "poutcome": "success",
        "emp.var.rate": 3,
        "cons.price.idx": 93,        
        "nr.employed": 5000
      }

df = pd.json_normalize(data)

st.write(model.predict(df))
