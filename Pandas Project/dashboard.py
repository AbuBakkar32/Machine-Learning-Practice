import kwargs as kwargs
import streamlit as st
import pandas as pd

st.title("Dashboard for Fake And Real News Detection")


@st.cache
def load_data():
    data = pd.read_csv('True_False_data.gz')
    return data


data = load_data()
if st.checkbox('Show Data'):
    data

st.bar_chart(data)

Sex = st.sidebar.multiselect("Groupe By Analysis", data.subject.value_counts())
# if Sex:
#     data = data[data.subject.isin(list(Sex))]
#     st.vega_lite_chart(data, {
#         'width': 'container',
#         'height': 400,
#         'mark': 'circle',
#         'encoding': {
#             'x': {
#                 'field': 'Age',
#                 'type': 'quantitative'
#             },
#             'y': {
#                 'field': 'Fare',
#                 'type': 'quantitative'
#             },
#             'size': {
#                 'field': 'Age',
#                 'type': 'quantitative'
#             },
#             'color': {
#                 'field': 'Content Rating',
#                 'type': 'nominal'}
#         }
#     }, use_container_width=True)

# else:
#     st.vega_lite_chart(data, {
#         'width': 'container',
#         'height': 400,
#         'mark': 'circle',
#         'encoding': {
#             'x': {
#                 'field': 'Age',
#                 'type': 'quantitative'
#             },
#             'y': {
#                 'field': 'Fare',
#                 'type': 'quantitative'
#             },
#             'size': {
#                 'field': 'Age',
#                 'type': 'quantitative'
#             },
#             'color': {
#                 'field': 'Content Rating',
#                 'type': 'nominal'}
#         }
#     }, use_container_width=True)

# st.dataframe(data.style.highlight_max(axis=0))
# st.line_chart(Sex)
# st.bar_chart(data.Fare)