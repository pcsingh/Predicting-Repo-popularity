# Predicting-Repo-popularity
Machine model that can predict the popularity of GitHub repository using it's title and some other stuffs as input. Here, popularity means the number of stars ✨ it can get. So, for data we use scripts to scrap data from github.

Folder `datasets` contains data files and script to extract data. And then the `final_data.csv` contains all the combine data of repositories which has columns `repo_name`, `star`, `fork`, `watch`, `issue`, `tags`, `language`, `discription`, `contributors`, `license`, and `repo_url`.

Analysis.ipynb :open_file_folder: file contains script to extract repositories most used languages using the repo url. And some plots regarding the dataset.

Then we will clean it and do some analysis to get insights according to that we will do featuring engineering and build model. Number of stars is a continuous variable so for building model we will use a ` supervised regression` algorithms.


Let's start :smile:
