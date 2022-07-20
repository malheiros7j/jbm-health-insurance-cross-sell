import pickle
import inflection
import pandas as pd
import numpy as np
import datetime


class Insurance_All(object):

    def __init__(self):

        self.home_path = '/home/jordanmalheiros/Estudismo/PA/PA004_jordan_malheiros/'

        self.frequency_encoder_policy_sales_channel =  pickle.load(open(self.home_path + 'features/frequency_encoder_policy_sales_channel.pkl','rb'))
        self.standard_annual_premium =                 pickle.load(open(self.home_path + 'features/standard_annual_premium.pkl','rb'))
        self.target_encoder_region_code =              pickle.load(open(self.home_path + 'features/target_encoder_region_code.pkl','rb'))
        self.mms_age =                                 pickle.load(open(self.home_path + 'features/mms_age.pkl','rb'))
        self.mms_vintage =                             pickle.load(open(self.home_path + 'features/mms_vintage.pkl','rb'))

    def data_cleaning(self,df1):

        df1.columns = ['id','gender','age','driving_license','region_code','previously_insured','vehicle_age','vehicle_damage','annual_premium','policy_sales_channel','vintage']

        return df1


    def featuring_engineering(self,df2):

        # IF custoemr vehicle was damage in the past -> 1 else ->
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x:1 if x == 'Yes' else 0)

        # Vehicle_age < 1 Year', '1-2 Year', '> 2 Years'
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'below_1_year' if x == '< 1 Year' else 'between_1_2_year' if x == '1-2 Year' else 'over_2_years')

        df2['gender'] = df2['gender'].apply(lambda x: x.lower())


        return df2



    def data_preparation(self,df5):

        # Standardization 

        # annual_premium
        df5['annual_premium'] = self.standard_annual_premium.transform(df5[['annual_premium']].values)

        # Reescaling 

        # age 
        df5['age'] = self.mms_age.transform(df5[['age']].values)

        # vintage
        df5['vintage'] = self.mms_vintage.transform(df5[['vintage']].values)


        # Encoding  |  | policy_sales_channel | gender 

        # region_code
        df5['region_code'] = df5['region_code'].map(self.target_encoder_region_code)

        # vehicle_age
        df5 = pd.get_dummies(df5,prefix='vehicle_age',columns=['vehicle_age'])

        # policy_sales_channel
        df5['policy_sales_channel']=df5['policy_sales_channel'].map(self.frequency_encoder_policy_sales_channel)

        # gender
        df5 = pd.get_dummies(df5,prefix='gender',columns=['gender'])

        cols_selected = ['vintage','annual_premium','age','region_code','vehicle_damage','policy_sales_channel','previously_insured']

        df5 = df5.fillna(0)

        return df5[cols_selected]




    def get_prediction(self,model,original_data,test_data):

        # Prediction

        pred = model.predict_proba(test_data)

        # Join Predict into the original data
        original_data['score_prediction'] = pred[:,1]
        original_data = original_data.sort_values('score_prediction',ascending=False)
        return original_data.to_json(orient='records',date_format='iso')

















