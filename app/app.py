import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DATABASE_URL)

def get_data():
    query = f"""
    SELECT * FROM public.commodities
        """
            
    df = pd.read_sql(query, engine)

    return df

st.set_page_config(page_title="Dahboard de Commodities", layout="wide")


st.title("Dahboard de Commodities")

st.write("""
    Este é um dashboard para visualizar os dados das commodities.
""")

df = get_data()

st.dataframe(df)



