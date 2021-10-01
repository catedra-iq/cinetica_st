import streamlit as st
import  generador_datos_sinteticos
import download
st.title('Práctica de Cinética')
df,i=generador_datos_sinteticos.main()
st.write(df)
st.write(i)
st.markdown(download.get_table_download_link(df,i), unsafe_allow_html=True)
