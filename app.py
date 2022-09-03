from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
app = Flask(__name__)
model = pickle.load(open('rf_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

df = pd.read_csv('car data.csv')
df['Car_age'] = 2020-df['Year']
df.drop(labels='Year',axis=1,inplace=True)
df = df.drop(labels='Car_Name', axis=1)
clean_data = pd.get_dummies(df,drop_first=True)
data_no_multicolinearity = clean_data.drop(['Fuel_Type_Petrol'],axis=1)
X = data_no_multicolinearity.drop('Selling_Price',axis=1)

min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X[['Present_Price','Car_age','Kms_Driven']])

@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Car_age= 2022 - Year
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        value=[[float(Present_Price), int(Car_age), int(Kms_Driven)]]
        scaled_value = min_max_scaler.transform(value)
        Present_Price = scaled_value[0,0]
        Car_age = scaled_value[0,1]
        Kms_Driven = scaled_value[0,2]
        # Kms_Driven2=min_max_scaler.transform(Kms_Driven)
        # Owner=int(request.form['Owner'])
        Fuel_Type_Diesel=request.form['Fuel_Type_Diesel']
        if(Fuel_Type_Diesel=='Diesel'):
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Diesel=0
        # Year=2021-Year
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
            # [[price, age, kms, fuel, Seller, trans]]
        prediction=model.predict([[Present_Price,Car_age,Kms_Driven,Fuel_Type_Diesel,Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You can sell your Car at {} Lakhs".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

