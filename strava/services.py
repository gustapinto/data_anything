import pandas as pd


dataframe = pd.read_json('./datasets/bike_rides.json')

def get_line_average(field):
    return f'{dataframe.loc[field].mean(axis=0):0.02f}'

def print_average_data():
    print(f'''
    Quilometragem média: {get_line_average('mileage')} Km
    Tempo médio por pedalada: {get_line_average('time')} m:s
    Velocidade normal média: {get_line_average('average_speed')} Km/h
    Velocidadade máxima média: {get_line_average('top_speed')} Km/h
    ''')

def plot_chart(field, title, kind):
    return dataframe.loc[field].plot(kind=kind, title=title)
