import base64
import numpy as np
def get_table_download_link(df,i):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="practica{np.random.randint(1,1333333)}{i}.csv">Descargar archivo</a>'
    return href