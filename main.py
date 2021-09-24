import pandas as pd

def casos(ruta_archivo: str)-> dict:
    data = pd.read_csv(ruta_archivo)
    data['Sexo'] = data['Sexo'].replace('f', 'F')
    data['Sexo'] = data['Sexo'].replace('m', 'M')
    PromeDepart=data.groupby('Departamento o Distrito').agg({'Edad':'mean'})
    PromeDepart=PromeDepart.round(4)
    PorcenSexo=data.groupby('Sexo').agg({'Sexo':'count'})
    PorcenSexo['Porcentaje']=(PorcenSexo['Sexo']*100)/len(data['Sexo'])
    PorcenSexo=PorcenSexo.round(4)
    porcen=data[data['Tipo']=='Importado']
    porcen=porcen.groupby('País de procedencia').agg({'País de procedencia':'count'})
    porcen['Porcentaje']=(porcen['País de procedencia']*100)/len(data[data['Tipo']=='Importado'].index)
    porcen=porcen.round(4)
    
    dicct3=porcen.to_dict()
    dicct3= dicct3['Porcentaje']
    dicct2=PromeDepart.to_dict()
    dicct2=dicct2['Edad']
    dicct=PorcenSexo.to_dict()
    dicct= dicct['Porcentaje']
    return([dicct, dicct2, dicct3])
