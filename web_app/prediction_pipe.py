from clean_new_data import clean_new
import pickle
import requests
import pandas as pd

r = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point')
data_point = r.json()

def get_prediction(data_point, thresholds=[.33,.67]):
    rfc = pickle.load(open('rfc.pkl', 'rb'))
    tfidf = pickle.load(open('text_tfidf.pkl', 'rb'))
    nb = pickle.load(open('text_nb.pkl', 'rb'))
    item = clean_new(data_point)
    vec = tfidf.transform(item['description'])
    vec = vec.todense()
    text_pred = nb.predict(vec)[0]
    item['NB_pred'] = text_pred
    item.drop(['description'], inplace=True, axis=1)
    item = item.fillna(0)
    pred = rfc.predict(item.values)[0]
    proba = rfc.predict_proba(item.values)[0][1]
    if proba > thresholds[1]:
        risk = 'high'
    elif proba < thresholds[0]:
        risk = 'low'
    else:
        risk = 'moderate'
    #return 'Fraud risk is {} -- {}%  chance of fraud'.format(risk, proba*100.)
    return risk, proba



if __name__ == '__main__':
    print get_prediction(data_point)
