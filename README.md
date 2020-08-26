# Predicting-Repo-popularity

Machine learning model that can predict the popularity of GitHub repository just by giving your repo URL in the input. Here, popularity means the number of stars ✨ it can get in the future. So, for data we use scripts to scrap data from github.

Folder `datasets` contains data files and script to extract data. And then the `final_data.csv` contains all the combine data of repositories which has columns `repo_name`, `star`, `fork`, `watch`, `issue`, `tags`, `most_used_lang`, `discription`, `contributors`, `license`, and `repo_url`.

combine.ipynb :open_file_folder: file contains script to extract repositories most used languages using the repo url. Analysis.ipynb file contains cleaning and visualization operations on the dataset. Now we are moving towards building a machine learning model that can predict which repositories will be starred by how much `star` in the future. 😃

Let's start 😊.
