import pandas as pd


data_frame = pd.read_json('./datasets/climate_data.json')
labels = {
    'min': 'Mínimas',
    'max': 'Máximas',
}

def _get_month_based_data_frame_by_year(desired_data, year):
    values = {'months':[], 'averages':[]}

    for month in data_frame.index:
        month_index = data_frame.index.get_loc(month)
        year_index = data_frame.columns.get_loc(year)

        values['months'].append(month)
        values['averages'].append(data_frame.values[month_index][year_index][desired_data])

    return pd.DataFrame({
        'Mêses': values['months'],
        f'{labels[desired_data]}': values['averages'],
    })

def plot_month_chart(desired_data, year, kind):
    plot_data_frame = _get_month_based_data_frame_by_year(desired_data, year)

    return plot_data_frame.plot(kind=kind,
                                title=f'{labels[desired_data]} {year}',
                                y=plot_data_frame.columns[1],
                                x=plot_data_frame.columns[0])
