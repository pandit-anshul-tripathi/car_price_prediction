import numpy as np
import pandas as pd
import streamlit as st
def app(cars_df):
	st.header('View Data')
	with st.beta_expander('View Dataset'):
		st.table(cars_df)
	st.subheader('Column Description:')
	if st.checkbox('Show Summary'):
		st.table(cars_df.describe())
	beta_col1, beta_col2, beta_col3 = st.beta_columns(3)
	with beta_col1:
		if st.checkbox('Show all columns names'):
			st.table(cars_df.columns)
	with beta_col2:
		if st.checkbox('View column data'):
			column_data = st.selectbox('Select column', tuple('enginesize', 'horsepower', 'carwidth', 'drivewheel_fwd', 'price'))
			if column_data == 'enginesize':
				st.write(cars_df['enginesize'])
			elif column_data == 'horsepower':
				st.write(cars_df['horsepower'])
			elif column_data == 'carwidth':
				st.write(cars_df['carwidth'])
			elif column_data == 'drivewheel_fwd':
				st.write(cars_df['drivewheel_fwd'])
			else:
				st.write(cars_df['price'])
	with beta_col3:
		if st.checkbox("View column data-type"):
			st.table(cars_df.dtypes)
