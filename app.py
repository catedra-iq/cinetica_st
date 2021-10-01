import streamlit as st
import  generador_datos_sinteticos
import download
st.title('Práctica de Cinética')
df=generador_datos_sinteticos.main()
st.write(df)
st.markdown(download.get_table_download_link(df), unsafe_allow_html=True)
