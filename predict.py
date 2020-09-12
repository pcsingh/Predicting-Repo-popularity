import pandas as pd
import pickle
import requests
import numpy as np
from bs4 import BeautifulSoup 
import nltk

header={'Accept':'application/vnd.github.mercy-preview+json',
'visibility':'PUBLIC'
}
with open('objs.pkl','rb') as f:  
    store_tag,vocabulary,word_dict = pickle.load(f)
with open('train_model.pkl','rb') as f: 
    model =pickle.load(f)

user_name=input("Enter username:")
repo_name=input("enter repo name:")
r=requests.get('https://github.com/pcsingh/WhatsApp-Chat-Analyzer/stargazers',headers=header)
soup = BeautifulSoup(r.content,features="lxml")
a=soup.find_all('li',class_='follow-list-item float-left border-bottom')
names=[]
for t in a:
    names.append(t.find_all('a',{'data-octo-click':'hovercard-link-click'})[-1].text)
i=0
if user_name not in  names:
    print("Star the repo(name) then try again :)")
    exit(1)

request=requests.get('https://api.github.com/repos/'+user_name+'/'+repo_name,headers=header)
data=request.json()
keys=['forks','watchers','open_issues_count','topics','description','language']
dataf=[data[k] for k in keys]
if str(data['license']).lower()=='none' or data['license']:
    license=0
else:
    license=1

request=requests.get('https://api.github.com/repos/'+user_name+'/'+repo_name+'/contributors',headers=header)
dat=request.json()
contributors=len(dat)
dataf.append(contributors)
dataf.append(license)
df=pd.DataFrame([dataf],columns=['fork','watch','issue','tags','description','most_used_lang','contributers','license'])
def perc(tags):
    sum_of_perc=0
    for tag in tags:
        if tag in store_tag:
            sum_of_perc+=(store_tag[tag]/vocabulary)
   
    return (sum_of_perc*100)

df['tag_ratio']=df['tags'].apply(perc).astype(float)
text=nltk.word_tokenize(df['description'][0])
tex=nltk.word_tokenize(repo_name)
def string_num(text):
    string_numbers=0
    for string in text:
        if string in word_dict:
            string_numbers+=word_dict[string]
    return string_numbers
df['desc_to_num']=string_num(text)
df['repo_to_num']=string_num(tex)
word_counts_for_language = {unique_word: [0] for unique_word in vocabulary}
df['most_used_lang']=df['most_used_lang'].str.split()
for word in df['most_used_lang']:
    if word[0] in word_counts_for_language:
        word_counts_for_language[word.lower()][index] += 1

language_col=pd.DataFrame(word_counts_for_language)
test_set=pd.concat([df,language_col],axis=1)
test_set.drop(['tags','description','language','no','most_used_lang'],axis=1,inplace=True)
model=pickle.load(open('model.sav','rb'))
print("your repo Popularity:",model.predict(test_set)[0])