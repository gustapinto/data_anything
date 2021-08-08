from datetime import datetime

from pandas import read_json, DataFrame
from numpy import mean


data_frame = read_json(path_or_buf='./datasets/bike_rides.json')

data_frame_labels = {
    'mileage': ['Quilometragem', 'Km'],
    'time': ['Tempo por pedalada', 'min'],
    'average_speed': ['Velocidade média', 'Km/h'],
    'top_speed': ['Velocidade máxima', 'Km/h'],
}

def _get_field_values_list(field: str, callback=None) -> list:
    values = data_frame.loc[field].values

    if (callback):
        return list(map(callback, values))

    return values

def _get_line_average_value(field: str) -> float:
    return mean(_get_field_values_list(field))

def _get_field_average_list(field: str) -> list:
    avg = _get_line_average_value(field)

    avg_list = [avg] * len(data_frame.columns)

    return avg_list

def _make_time_visible_on_chart(time: int) -> int:
    return time * 10

def print_average_data():
    for element, labels in data_frame_labels.items():
        label = labels[0]
        metric_unit = labels[1]

        average = _get_line_average_value(element)

        if element == 'time':
            average /= 60  # Convert seconds to minutes
        elif element == 'mileage':
            average /= 1000  # Convert meters to kilometers

        print(f'{label}: {average:0.02f} {metric_unit}')

def plot_mileage_chart():
    plot_data = DataFrame({
        'Datas': data_frame.columns,
        'Duração': _get_field_values_list('time', _make_time_visible_on_chart),
        'Metragem': _get_field_values_list('mileage'),
        'Metragem Média': _get_field_average_list('mileage'),
    })

    time_sub_plot = plot_data.plot(x='Datas', y='Duração', color='#ffc107',
                                   use_index=True, kind='line')

    avg_and_time_sub_plot = plot_data.plot(x='Datas', y='Metragem Média', color='#ed8121',
                                           ax=time_sub_plot, use_index=True,
                                           kind='line')

    plot_data.plot(x='Datas', y='Metragem', ax=avg_and_time_sub_plot,
                   kind='bar')

def plot_all_rides_table():
    df = data_frame.transpose().rename(columns={
        'mileage': 'Quilometragem',
        'time': 'Duração',
        'average_speed': 'Velocidade média',
        'top_speed': 'Velocidade máxima',
    })
    
    return df.style.format(precision=2, formatter={
        ('Quilometragem'): lambda mileage: '{:.2f} Km'.format(mileage / 1000),
        ('Duração'): lambda seconds: '{:.2f} Min'.format(seconds / 60),
        ('Velocidade média'): lambda speed: '{:.1f} Km/h'.format(speed),
        ('Velocidade máxima'): lambda speed: '{:.1f} Km/h'.format(speed),
    })
