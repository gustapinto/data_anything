import pandas as pd


data_frame = pd.read_json(path_or_buf='./datasets/bike_rides.json')

data_frame_labels = {
    'mileage': ['Quilometragem', 'Km'],
    'time': ['Tempo por pedalada', 'm:s'],
    'average_speed': ['Velocidade média', 'Km/h'],
    'top_speed': ['Velocidade máxima', 'Km/h'],
}

def _get_line_average(field):
    return data_frame.loc[field].mean(axis=0)

def _parse_data_frame_for_plot(field):
    field_avg = []
    field_label = data_frame_labels[field][0]

    for key in data_frame.columns:
        field_avg.append(_get_line_average(field))

    plot_data_frame = pd.DataFrame({
        'Datas': data_frame.columns,
        'Média': field_avg,
        field_label: data_frame.loc[field].values,
    })

    return plot_data_frame

def print_average_data():
    for element, labels in data_frame_labels.items():
        label = labels[0]
        metric_unit = labels[1]

        print(f'{label}: {_get_line_average(element):0.02f} {metric_unit}')

def plot_chart(field, kind):
    plot_data = _parse_data_frame_for_plot(field)
    plot_index = True if kind != 'bar' else False

    field_label = data_frame_labels[field][0]

    sub_plot = plot_data.plot(x='Datas', y='Média', color='#ed8121',
                              use_index=plot_index)

    return plot_data.plot(x='Datas', y=field_label, ax=sub_plot,
                          kind=kind, title=field_label)
