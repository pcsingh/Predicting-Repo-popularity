# Predicting-Repo-popularity

<img src="media/sample.gif" width="900" height="430" />

Machine learning model that can predict the popularity of GitHub repository just by giving your repo URL in the input. Here, popularity means the number of stars ✨ it can get in the future. So, for data we use scripts to scrap data from github.

Folder `Notebooks` contains data and script to extract data, analysis of data or the model creation code. We have used github api and Kaggle to collect the github data stored in the  file `github_api.csv` and `kaggle_data.csv` respectively which has columns `repo_name`, `star`, `fork`, `watch`, `issue`, `tags`, `most_used_lang`, `discription`, `contributors`, `license`, and `repo_url`.

`data_extraction.ipynb` file contains script to extract the information from repositories, `analysis.ipynb` file contains cleaning and visualization operations on the dataset. `model.ipynb` building a machine learning model that can predict which repositories will gain how much `stars` in the future. 😃

## Run on Local System

* Create an virual environment:
```
python -m venv "evironment_name"
```
For more details follow [this link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

* Activate the Environment:
  - For Windows:
     > .\"evironment_name"\Scripts\activate

  - For Mac or Linux:
    > source "evironment_name"/bin/activate


* Install the required dependencies: 
```
pip install -r requirement.txt
```

*  Clone the repository:
```
git clone https://github.com/pcsingh/Predicting-Repo-popularity.git
```
* Enter into the directory:
```
cd Predicting-Repo-popularity
```


1. To extract the  github repo data using github api run [data_extraction.ipynb](https://github.com/pcsingh/Predicting-Repo-popularity/blob/master/Notebooks/data_extraction.ipynb) notebook.
<br>
Github has the limits on the number of requests using github api, so you need to use your github token in order to extract data.One can generate their github token from [here](https://github.com/settings/tokens).

Replace the `PASTE_YOUR_GITHUB_TOKEN_HERE` with your github token.

GitHub api requires headers for authorization.<br>

```
header={'Accept':'application/vnd.github.mercy-preview+json',
'visibility':'PUBLIC',
"Authorization": "token PASTE_YOUR_GITHUB_TOKEN_HERE"
} 
```

2. To visualize some insight of the dataset run [analysis.ipynb](https://github.com/pcsingh/Predicting-Repo-popularity/blob/master/Notebooks/analysis.ipynb)

3. For training the model run [model.ipynb](https://github.com/pcsingh/Predicting-Repo-popularity/blob/master/Notebooks/model.ipynb) file, we have used multiple regressions model, but one with the best R2 score is used for making prediction.<br><br>
* Run streamlit in order to make prediction using trained model:
```
streamlit run app.py
```

**Note: Remember to paste the github token in the model.ipynb notebook and app.py file.**
<hr>

Click [here](https://repopopularity.herokuapp.com/) to try now..... 🤗
