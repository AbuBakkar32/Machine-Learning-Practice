import bar_chart_race as bcr
df = bcr.load_dataset('covid19_tutorial')
bcr.bar_chart_race(df=df, filename='covid-19.mp4', n_bars=10, period_fmt='%B %d, %Y', title='COVID-19 Confirmed Cases by Country')

# bcr.bar_chart_race(
#     df=df,
#     filename='covid19_horiz.mp4',
#     orientation='h',
#     sort='desc',
#     n_bars=6,
#     fixed_order=False,
#     fixed_max=True,
#     steps_per_period=10,
#     interpolate_period=False,
#     label_bars=True,
#     bar_size=.95,
#     period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
#     period_fmt='%B %d, %Y',
#     period_summary_func=lambda v, r: {'x': .99, 'y': .18,
#                                       's': f'Total deaths: {v.nlargest(6).sum():,.0f}',
#                                       'ha': 'right', 'size': 8, 'family': 'Courier New'},
#     perpendicular_bar_func='median',
#     period_length=500,
#     figsize=(5, 3),
#     dpi=144,
#     cmap='dark12',
#     title='COVID-19 Deaths by Country',
#     title_size='',
#     bar_label_size=7,
#     tick_label_size=7,
#     scale='linear',
#     writer=None,
#     fig=None,
#     bar_kwargs={'alpha': .7},
#     filter_column_colors=False)


# df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv/data.csv')
# df = df[['dateRep', 'countriesAndTerritories', 'cases']]
# df['date'] = pd.to_datetime(df['dateRep'], dayfirst=True)
# df['total_cases'] = df.sort_values('date').groupby('countriesAndTerritories').cumsum().sort_index()
# df = df[['date', 'countriesAndTerritories', 'total_cases']]
# df = df.rename(columns={'countriesAndTerritories': 'country'})
# df = pd.pivot_table(df, index=['date'], columns=['country'], values=['total_cases'])
# df.index.name = None
# df.columns = [col[1] for col in df.columns]
# df = df.fillna(0).astype(int)
# df = df.drop(columns=['Cases_on_an_international_conveyance_Japan'])
# df.columns = [col.replace('_', ' ') for col in df.columns]
#
# # Country Remove
# country_reserved = set()
# for index, row in df.iterrows():
#     country_reserved |= set(row[row > 0].sort_values(ascending=False).head(10).index)
# df = df[list(country_reserved)]


