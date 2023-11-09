import pandas as pd

# Nome do arquivo CSV de entrada
input_file = r'caminho_csv_para_dividir'

# Número de linhas por arquivo de saída
linhas_por_arquivo = 1900000  # Defina o número desejado

# Ler o arquivo CSV de entrada em um DataFrame
df = pd.read_csv(input_file)

# Dividir o DataFrame em pedaços menores
chunks = [df[i:i + linhas_por_arquivo] for i in range(0, len(df), linhas_por_arquivo)]

# Salvar cada pedaço em arquivos CSV separados
for i, chunk in enumerate(chunks, start=1):
    output_file = f'caminho_de_saida/arquivo_saida_{i}.csv'
    chunk.to_csv(output_file, index=False)

print("Arquivos divididos com sucesso.")
