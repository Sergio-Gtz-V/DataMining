import pandas as pd

#Leemos el archivo descargado de la primera practica
df = pd.read_csv('downloaded_file.csv')

#Limpieza de columnas

df = df.drop(['GAME_STATUS_TEXT','HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'TEAM_ID_home', 'TEAM_ID_away'], axis = 1)

df.to_csv('cleaned_database.csv', index=False)

