# Car Price Prediction
Deployed here -> https://predicting-carprice.herokuapp.com/
## Predicting the Price of Used Cars
*On Car Dekho Dataset*<br>

In this Project, we are going to predict the Price of Used Cars using various features like Present_Price, Selling_Price, Kms_Driven, Fuel_Type, Year etc. The data used in this project was downloaded from Kaggle.

**To be able to predict used cars market value can help both buyers and sellers.**

There are lots of individuals who are interested in the used car market at some points in their life because they wanted to sell their car or buy a used car. In this process, it’s a big corner to pay too much or sell less then it’s market value.

## Steps:
1. Data Collection and Loading
2. Data Cleaning 
3. Data Pre Processing (Data Normalisation)
4. Data Selection (Using VIF and F-test)
5. EDA (Exploratory Data Analysis)
6. Prediction
7. Algorithms Used:
   * Multiple Linear Regression
   * Random Forest Regressor
   * Randomized Search CV (with Random Forest Regressor)
8. Accuracy Measured using R square Method
8. Serialized the Model using Pickle
9. Deployed on Flask
10. Hosted on Heroku Platform

## Conclusions:
* Present price of a car plays an important role in predicting Selling Price, One increases the other gradually increases.
* Car age is effecting negatively as older the car lesser the Selling Price.
* Selling Price of cars with Fuel type Diesel is higher.
* Car of Manual type is of less priced whereas of Automatic type is high.
* Cars sold by Individual tend to get less Selling Price when sold by Dealers.
