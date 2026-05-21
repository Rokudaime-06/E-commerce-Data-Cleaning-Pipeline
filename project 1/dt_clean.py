import numpy as np
import pandas as pd
import random

# Génération d'un gros fichier mrewen (100 lignes)
np.random.seed(42)
n_rows = 100

data_complex = pd.DataFrame({
    " ORDER_ID  ": [f"ID_{1000 + i}" for i in range(n_rows)],
    "product_name": random.choices(["iphone 15", "Samsung S24", "MacBook Pro", "iPad Air", "AirPods Pro"], k=n_rows),
    "quantity": [random.choice([1, 2, 3, np.nan, 5, -1, 10]) for _ in range(n_rows)], # fih negative w NaN
    "item_price": [random.choice(["799 $", "999 $", "1499 $", "599 $", "249 $", "missing", ""]) for _ in range(n_rows)], # fih le symbole $ w faux vides
    "purchase_date": [random.choice(["2026/05/15", "15-05-2026", "2026-05-16", "unknown", None]) for _ in range(n_rows)], # formats mkhwda w unknown
    "customer_email": [f"user_{i}@gmail.com" if i % 10 != 0 else f"USER_{i}@GMAIL.COM  " for i in range(n_rows)]
})

# Zdna des doublons complètement
data_complex = pd.concat([data_complex, data_complex.iloc[:5]], ignore_index=True)

# Sauvegarde f ton PC
data_complex.to_csv("ecom_sales_raw.csv", index=False)
print("🎯 Le fichier 'ecom_sales_raw.csv' est créé f ton folder local !")

#_______Data cleaning_______#

#1.exploration de data

data_complex.info()
print(data_complex.head())
print(data_complex.describe())

#2.structuration:

print("_"*100)
data_complex = data_complex.drop_duplicates()
data_complex = data_complex.rename(columns={"product_name":"Product name", "item_price":"Item price", "purchase_date":"Purchase date", "customer_email":"Customer email"})
data_complex = data_complex.rename(columns={"ORDER_ID": "Order Id"})
data_complex.columns = data_complex.columns.str.strip()
print(data_complex.to_string(index=False))
print("_"*100)

#3.les valeurs qui manquent:

data_complex = data_complex.replace(["unknown", "None", -1.0, "missing", "", ], np.nan)


#4.standardisation:

data_complex["ORDER_ID"] = data_complex["ORDER_ID"].astype(str).str.strip().str.capitalize()
data_complex["Product name"] = data_complex["Product name"].astype(str).str.strip().str.capitalize()
data_complex["quantity"] = data_complex["quantity"].astype(str)
data_complex["Item price"] = data_complex["Item price"].astype(str)
data_complex["Purchase date"] = data_complex["Purchase date"].astype(str)
data_complex["Customer email"] = data_complex["Customer email"].astype(str).str.strip().str.capitalize()
data_complex["Purchase date"] = data_complex["Purchase date"].replace({"None": "_", "nan":"_" })
data_complex["Item price"] = data_complex["Item price"].str.replace("$", "", case=False)

print("the table after modification:")
print(data_complex.to_string(index=False))