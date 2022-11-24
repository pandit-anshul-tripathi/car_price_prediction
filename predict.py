import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from slearn.metrics import mean_squared_error as mse, r2_score, mean_absolute_error as mae, mean_squared_log_error as msle
@st.cache()
def prediction(cars_df, car_width, engine_size, horse_power, dwf, ccb):
	X = cars_df.iloc[:, :-1]
	y = cars_df['price']
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
	lin_reg = LinearRegression()
	lin_reg.fit(X_train, y_train)
	score = lin_reg.score(X_train, y_train)
	price_pred = lin_reg.predict([[car_width, engine_size, horse_power, dwf, ccb]])
	price_pred = price_pred[0]
	y_test_pred = lin_reg.predict(X_test)
	test_r2_score = r2_score(y_test, y_test_pred)
	test_mse = mse(y_test, y_test_pred)
	test_mae = mae(y_test, y_test_pred)
	test_msle = msle(y_test, y_test_pred)
	return price_pred, test_r2_score, test_mse, test_mae, test_msle
def app(cars_df):
	st.markdown('<p style = "color:blue;font-size:25px"> This App uses <b> Linear Regression </b> to predict the price of a car based on your inputs.</p>', unsafe_allow_html = True)
	st.subheader('Select Values')
	car_w = st.slider('Car Width', float(cars_df['carwidth'].min()), float(cars_df['carwidth'].max()))
	car_hp = st.slider('Horse Power', float(cars_df['horsepower'].min()), float(cars_df['horsepower'].max()))
	car_es = st.slider('Engine Size', float(cars_df['enginesize'].min()), float(cars_df['enginesize'].max()))
	car_dwf = st.radio('Is it a forward drive wheel car ?', tuple('Yes', 'No'))
	if car_dwf == 'No':
		car_dwf = 0
	else:
		car_dwf = 1
	car_ccb = st.radio('Is the car manufactures by Buick', tuple('Yes', 'No'))
	if car_ccb == 'No':
		car_ccb = 0
	else:
		car_ccb = 1
	if st.button('Predict'):
		st.subheader('Prediction Results')
		price, r2, mse, mae, msle = prediction(cars_df, car_w, car_es, car_hp, car_dwf, car_ccb)
		st.success('The price of car in dollars is ', int(price))
		st.info(f'R2 score of the model is:{r2}')
		st.info(f'MSE of the model:{mse:.3f}')
		st.info(f'MAE of the model:{mae:.3f}')
		st.info(f'MSLE of the model:{msle:.3f}')
