import pandas as pd


class CSVFileManager:
  """S'encarrega de llegir i escriure un fitxer CSV"""
  
  def __init__(self, path: str):
    """Guarda la ruta on és el CSV"""
    self.path = path
    
  def read(self) -> pd.DataFrame:
    """Llegirà el CSV i ens el retornarà com a DataFrame"""
    return pd.read_csv(self.path)
    
  def write(self, dataFrame):
    """És opcional, ens guarda un DataFrame al CSV"""
    pass
