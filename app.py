import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np
from bs4 import BeautifulSoup 
import nltk

header={'Accept':'application/vnd.github.mercy-preview+json',
'visibility':'PUBLIC',
"Authorization": "token put_your_token"
}
st.markdown(f'<h1 style="text-align:center;color:#929aab;font-family:Bitter;font-size:54px;margin-bottom:20px">Github Repo Popularity <br>Prediction</h1>', unsafe_allow_html=True)

st.image('original.gif')

with open('objs.pkl','rb') as f:  
    store_tag,vocabulary,vocab,word_dict = pickle.load(f)
with open('train_model.pkl','rb') as f: 
    model =pickle.load(f)

def perc(tags):
        sum_of_perc=0
        for tag in tags:
            print(tag)
            if tag in store_tag:
               
                sum_of_perc+=(store_tag[tag]/vocabulary)
    
        return (sum_of_perc*100)
def string_num(text):
    string_numbers=0
    for string in text:
        if string in word_dict:
            string_numbers+=word_dict[string]
    return string_numbers

st.sidebar.text("This is the project to predict the \nrepo popularity using 'Forks','Watcher',\n'Issues','Tags','Description of Repo',\n'Contributers', License' and the \nlanguage used for project. \nThe data has been collected using web \nscraping ,Github api and kaggle github \ndatasets, then Machine learning \nRegression is used to predict the\nRepo Popularity.")
keys=['forks','watchers','open_issues_count','topics','description','language']
form = st.form(key='my_form')
user_name = form.text_input("Username")
repo_name= form.text_input("Repo name")
submit_button = form.form_submit_button(label='Predict')
if submit_button:
    try:
        user_name=user_name.strip()
        repo_name=repo_name.strip()
        request=requests.get('https://api.github.com/repos/'+user_name+'/'+repo_name,headers=header)
        data=request.json()
       
        dataf=[data[k] for k in keys]
        if str(data['license']).lower()=='none':
            license=0
        else:
            license=1
            
        request=requests.get('https://api.github.com/repos/'+user_name+'/'+repo_name+'/contributors',headers=header)
        dat=request.json()
        contributors=len(dat)
        dataf.append(contributors)
        dataf.append(license)
        df=pd.DataFrame([dataf],columns=['fork','watch','issue','tags','description','most_used_lang','contributers','license'])
        
        
        df['most_used_lang']=df['most_used_lang'].str.lower()
    
        df['description']=df['description'].str.lower()
        df['tag_ratio']=df['tags'].apply(perc).astype(float)
        
        if df['description'][0]:
            text=nltk.word_tokenize(df['description'][0])
            df['desc_to_num']=string_num(text)
        else:
            df['desc_to_num']=0
        word_counts_for_language = {unique_word: [0] for unique_word in vocab}
        df['most_used_lang']=df['most_used_lang'].str.split()
        for word in df['most_used_lang']:
            if word[0] in word_counts_for_language:
                word_counts_for_language[word[0].lower()][0] += 1
        
        first_kpi, second_kpi, third_kpi,fourth= st.beta_columns(4)


        with first_kpi:
            st.markdown("**Issues**")
            number1 = data['open_issues']
            st.markdown(f"<h1 style=' color: red;'>{number1}</h1>", unsafe_allow_html=True)
        
        with second_kpi:
            st.markdown("**Watchers**")
            number2 = data['watchers']
            st.markdown(f"<h1 style=' color: red;'>{number2}</h1>", unsafe_allow_html=True)
        
        with third_kpi:
            st.markdown("**Forks**")
            number3 = data['forks']
            st.markdown(f"<h1 style=' color: red;'>{number3}</h1>", unsafe_allow_html=True)
        with fourth:
            st.markdown("**TAGs**")
            if data['topics']:
                number4 = data['topics']
            else:
                number4='Not mentioned'
            st.markdown(f"<h1 style=' color: red;'>{number4}</h1>", unsafe_allow_html=True)
        st.markdown(f"<hr>", unsafe_allow_html=True)
        first,sec= st.beta_columns(2)


        with first:
            st.markdown("**Description**")
            number1 = data['description']
            st.markdown(f"<p style=' color: red;'>{number1}</p>", unsafe_allow_html=True)
        with sec:
            st.markdown("**License**")
            
            st.markdown(f"<p style=' color: red;'>{data['license']}</p>", unsafe_allow_html=True)
        
        st.markdown(f"<hr>", unsafe_allow_html=True)
        language_col=pd.DataFrame(word_counts_for_language)
        test_set=pd.concat([df,language_col],axis=1)
        test_set.drop(['tags','description','language','no','most_used_lang'],axis=1,inplace=True)
        pred=int(model.predict(test_set)[0])
        if pred>1000:
            pred=str(float(pred)/1000)+'k'
        st.success("Your Repo can achieve Popularity  : "+str(pred)+' 🌟')
    
    except:
        st.error("Sorry cannot find the repo, please Try again!!!")