import hashlib

import pandas as pd

def gerar_chave(df, prefixo):

    if df.empty:
        raise ValueError("DataFrame vazio não pode gerar chave!")
    
    hash_dados = hashlib.md5(pd.util.hash_pandas_object(df).values).hexdigest()
    
    return f"{prefixo}_{hash_dados}"