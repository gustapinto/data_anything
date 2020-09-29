import pandas as pd


data_frame = pd.read_json(path_or_buf='./datasets/bike_rides.json')

labels = {
    'mileage': 'Quilometragem',
    'time': 'Tempo por pedalada',
}

def _get_line_average(field):
    return data_frame.loc[field].mean(axis=0)

def _parse_data_frame_for_plot(field):
    field_avg = []

    for key in data_frame.columns:
        field_avg.append(_get_line_average(field))

    plot_data_frame = pd.DataFrame({
        'Datas': data_frame.columns,
        labels[field]: data_frame.loc[field].values,
        'Media': field_avg,
    })

    return plot_data_frame

def print_average_data():
    print(f'''
Quilometragem média       | {_get_line_average('mileage'):0.02f} Km
Tempo médio por pedalada  | {_get_line_average('time'):0.02f} m:s
Velocidade normal média   | {_get_line_average('average_speed'):0.02f} Km/h
Velocidadade máxima média | {_get_line_average('top_speed'):0.02f} Km/h
    ''')

def plot_chart(field, kind):
    plot_data = _parse_data_frame_for_plot(field)

    if kind == 'bar':
        sub_plot = plot_data.plot(x='Datas', y='Media', color='#ed8121',
                                  use_index=False)
    elif kind == 'line':
        sub_plot = plot_data.plot(x='Datas', y='Media', color='#ed8121',
                                  use_index=True)

    return plot_data.plot(x='Datas', y=labels[field], ax=sub_plot,
                          kind=kind, title=labels[field])
