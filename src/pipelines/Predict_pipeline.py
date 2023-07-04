import sys
import os
import pandas as pd
from src.Exception import CustomException
from src.utils import load_object
from dataclasses import dataclass
# from flask import request
from src.logger import logging

import pandas as pd
from src.Exception import CustomException
from src.utils import load_object



class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='artifacts\preprocessor.pkl'
            preprocessor_path='Model\model.pkl'
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 limit_bal:int,
                 sex:int,
                 education:int,
                 marriage:int,
                 age:int,
                 pay_0:int,
                 pay_2:int,
                 pay_3:int,
                 pay_4:int,
                 pay_5:int,
                 pay_6:int,
                 bill_amt1:int,
                 bill_amt2:int,
                 bill_amt3:int,
                 bill_amt4:int,
                 bill_amt5:int,
                 bill_amt6:int,
                 pay_amt1:int,
                 pay_amt2:int,
                 pay_amt3:int,
                 pay_amt4:int,
                 pay_amt5:int,
                 pay_amt6:int):
        
        self.limit_bal = limit_bal # the amount of the given credit
        self.sex = sex # the gender of the client (1 = male, 2 = female)
        self.education = education # the education level of the client (1 = graduate school, 2 = university, 3 = high school, 4 = others)
        self.marriage = marriage # the marital status of the client (1 = married, 2 = single, 3 = others)
        self.age = age # the age of the client
        self.pay_0 = pay_0 # the repayment status in September 2005 (-1 = pay duly, 1 = payment delay for one month, etc.)
        self.pay_2 = pay_2 # the repayment status in August 2005
        self.pay_3 = pay_3 # the repayment status in July 2005
        self.pay_4 = pay_4 # the repayment status in June 2005
        self.pay_5 = pay_5 # the repayment status in May 2005
        self.pay_6 = pay_6 # the repayment status in April 2005
        self.bill_amt1 = bill_amt1 # the amount of bill statement in September 2005
        self.bill_amt2 = bill_amt2 # the amount of bill statement in August 2005
        self.bill_amt3 = bill_amt3 # the amount of bill statement in July 2005
        self.bill_amt4 = bill_amt4 # the amount of bill statement in June 2005
        self.bill_amt5 = bill_amt5 # the amount of bill statement in May 2005
        self.bill_amt6 = bill_amt6 # the amount of bill statement in April 2005
        self.pay_amt1 = pay_amt1 # the amount of previous payment in September 2005
        self.pay_amt2 = pay_amt2 # the amount of previous payment in August 2005
        self.pay_amt3 = pay_amt3 # the amount of previous payment in July 2005
        self.pay_amt4 = pay_amt4 # the amount of previous payment in June 2005
        self.pay_amt5 = pay_amt5 # the amount of previous payment in May 2005
        self.pay_amt6 = pay_amt6 


    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'limit_bal':[self.limit_bal],
                'sex':[self.sex],
                'education':[self.education],
                'marriage':[self.marriage],
                'age':[self.age],
                'pay_0':[self.pay_0],
                'pay_2': [self.pay_2],
                'pay_3': [self.pay_3],
                'pay_4': [self.pay_4],
                'pay_5': [self.pay_5],
                'pay_6': [self.pay_6],
                'bill_amt1':[self.bill_amt1],
                'bill_amt2': [self.bill_amt2],
                'bill_amt3': [self.bill_amt3],
                'bill_amt4': [self.bill_amt4],
                'bill_amt5': [self.bill_amt5],
                'bill_amt6': [self.bill_amt6],
                'pay_amt1':[self.pay_amt1],
                'pay_amt2': [self.pay_amt2],
                'pay_amt3': [self.pay_amt3],
                'pay_amt4': [self.pay_amt4],
                'pay_amt5': [self.pay_amt5],
                'pay_amt6': [self.pay_amt6],
            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
            print(df)
        
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)


