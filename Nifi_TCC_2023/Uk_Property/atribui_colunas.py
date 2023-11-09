import numpy as np
import pandas as pd
import sys
from datetime import datetime 
#!/usr/bin/python3

# Load the raw data
colnames=['Transaction_unique_identifier', 'price', 'Date_of_Transfer', 
          'postcode', 'Property_Type', 'Old_New', 
          'Duration', 'PAON', 'SAON', 
          'Street', 'Locality', 'Town_City', 
          'District', 'County', 'PPDCategory_Type',
          'Record_Status_monthly_file_only'
          ] 

file = pd.read_csv(r'C:\Users\filip\Desktop\data\testeeee.csv',
                header=None,
                names=colnames,
                infer_datetime_format=True,
                parse_dates=["Date_of_Transfer"],
                dayfirst=False
                )

file = file.drop(['PPDCategory_Type', 'Record_Status_monthly_file_only'], axis=1)
print(file.head(3))
#file.to_csv(sys.stdout, index=False)
