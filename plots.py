import matplotlib.pylot as plt
import seaborn as sns
import streamlit as st
def app(cars_df):
	st.header('Visualise Data')
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.subheader('Visualisation Selector')
	plot_types = st.multiselect('Select the type of the plot' ,tuple('Correlation Heatmap', 'Scatter Plot', 'Box Plot', 'Histogram'))
	if 'Correlation Heatmap' in plot_types:
		st.subheader('Correlation Heatmap')
		plt.figure(figsize=(12,6), dpi = 100)
		sns.heatmap(data = cars_df.corr(), annot = True)
		st.pyplot()
	if 'Scatter Plot' in plot_types:
		st.subheader('Scatter Plot')
		columns = st.multiselect('Select X axis Values', tuple('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
		for i in columns:
			st.subheader(f'Scatter Plot between {i} and Price')
			plt.figure(figsize=(12,6))
			sns.scatterplot(x = cars_df[i], y = cars_df['price'])
			st.pyplot()
	if 'Box Plot' in plot_types:
		st.subheader('Box Plot')
		columns = st.selectbox('Select the column for Box Plot', tuple('carwidth', 'enginesize', 'horsepower'))
		plt.figure(figsize=(12,6))
		plt.title(f'Box Plot for {columns}')
		sns.boxplot(cars_df[columns])
		st.pyplot()
	if 'Histogram' in plot_types:
		st.subheader('Histogram')
		columns = st.selectbox('Select the columns to create Histogram', tuple('carwidth', 'enginesize', 'horsepower'))
		plt.figure(figsize = (12,6))
		plt.histogram(cars_df[columns], bins = 'sturges', edgecolor = 'black')
		st.pyplot()
