import pandas as pd
import streamlit as st

dfCalificaciones = pd.read_excel("tareas.xlsx")

dfCalificaciones["promedio"] = ( dfCalificaciones["tarea1"] + dfCalificaciones["tarea2"] +
                                dfCalificaciones["tarea3"] + dfCalificaciones["tarea4"]) / 4
                                
dfCalificaciones["final"] = dfCalificaciones["promedio"].apply(lambda x: "Aprobado" if x >= 70 else "Reprobado")

dfResultados = dfCalificaciones[ ["matricula","promedio","final"] ]

dfResultados

st.dataframe(dfResultados)
