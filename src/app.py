# import Flask and jsonify
import flask
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api
import pandas as pd
import numpy as np
import pickle

# App definition
app = Flask(__name__)
api = Api(app)

# importing models
model = pickle.load(open("model.p", "rb" ))
model_columns = pickle.load(open( "columns.p", "rb" ))

class Predict(Resource):
    def get(self):
        if flask.request.method == 'GET':
            return "Prediction page. Try using POST with params to get specific prediction."
        
    def post(self):
        json_data = request.get_json()
        
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()

        # we need to make sure that we have all the columns that our model was trained on
        df = df.reindex(columns=model_columns, fill_value=0)

        Return = model.predict(df).tolist()
        
        if str(Return) == '[1]':
            Return = "Your loan status is approved! "+ str(Return)
        elif str(Return) == '[0]':
            Return = "Your loan status is approved! "+ str(Return)
        else:
            Return = "Request unsuccessful"
        
        return Return

# assign endpoint
api.add_resource(Predict, '/predict')

@app.route('/')
def welcome():
    return "Welcome! Use this Flask App for predicting loan status"

__name__ == '__main__'
app.run(debug=True, host='0.0.0.0', port=5000)




