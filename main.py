from flask import Flask, request
import pandas as pd

df = pd.read_csv('./data/services2019.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is an API service for MN ICD code details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result
    
@app.route('/icd/<value>', methods=['GET'])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['svc_code_ctg'] == value]
    return filtered.to_json(orient="records")



if __name__ =='__main__':
    app.run(debug=True)