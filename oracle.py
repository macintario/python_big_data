import pandas_oracle.tools as oradf

query1 = "select distinct rfc, hrs_nom from all_nom"
query2 = "select rfc, hrs_nom from all_nom"

## opening conn
conn = oradf.open_connection("config.yml")

## passing the conn object to the query_to_df
df1 = oradf.query_to_df(query1, conn, 10000)

## passing the conn object to the query_to_df , without to open again
df2 = oradf.query_to_df(query2, conn, 10)

print(df1['HRS_NOM'].sum())
print(df1['HRS_NOM'].mean())
print(df1['HRS_NOM'].median())

## close connection
oradf.close_connection(conn)