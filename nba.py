#Imported data manipulation library
import pandas as pd

#Create dataframe
nba = pd.read_csv("Duke.csv")

#Created ratio column
nba['Rebounds/Fouls'] = nba.apply(lambda row: row['TRB']/row['PF'] if row['PF'] != 0 else 0, axis=1)

#Created new df with only relevent data
df = pd.DataFrame() 
df['Player_Name'] = nba['Player'] 
df['Rebounds/Fouls'] = nba['Rebounds/Fouls']
print(type(df))
df.to_csv("Duke_2019-2020.csv")

