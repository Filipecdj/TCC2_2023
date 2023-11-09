import pandas as pd
import numpy as np
import sys
import io
#!/usr/bin/python3

file = pd.read_csv(sys.stdin)

# Função para ajustar as files
def adjust_date(date_str):
    parts = date_str.split('/')
    if len(parts) == 3:
        month, day, year = map(int, parts)
        return f'{day:02d}-{month:02d}-{year:02d}'
    else:
        return date_str

# Aplica a função de ajuste às files
file['Departure Date'] = file['Departure Date'].apply(adjust_date)
file['Departure Date'] = pd.to_datetime(file['Departure Date'], dayfirst=True)  # Ignora o aviso

# Cria a coluna id na tabela
start_id = 15
file = file.reset_index()
file = file.rename(columns={'index': 'id'})

# Incremente os valores do ID sequencialmente a partir de start_id
file['id'] = file.index + start_id

# Mapeie os nomes das colunas substituindo espaços por underscores
new_column_names = {col: col.replace(' ', '_') for col in file.columns}
file.rename(columns=new_column_names, inplace=True)

# Retorna o CSV tratado
file.to_csv(sys.stdout, index=False)


