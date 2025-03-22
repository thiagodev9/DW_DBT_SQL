# Import necessary libraries
import pandas as pd
import yfinance as yf
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv()

# import das minhas variaveis de ambiente
commodities = ['CL=F', 'GC=F', 'SI=F']

DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_SCHEMA=os.getenv('DB_SCHEMA')

DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URI)


def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados_commodity = buscar_dados_commodities(simbolo)
        todos_dados.append(dados_commodity)
    return pd.concat(todos_dados)

def salvar_no_postgres(df, schema='public'):
    df.to_sql('commodities',engine, if_exists='append', index=True, index_label='Date', schema=schema)

if __name__ == '__main__':
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    salvar_no_postgres(dados_concatenados, schema='public')
