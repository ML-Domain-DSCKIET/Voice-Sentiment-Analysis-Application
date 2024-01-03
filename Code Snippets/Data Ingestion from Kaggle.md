
### Data Ingestion from Kaggle
Datasets from platforms like Kaggle can be referred for carrying out machine learning experiments and modelling.
##### References:
1. https://www.kaggle.com/learn-guide/models-audio-data
2. https://huggingface.co/blog/audio-datasets

Instructions to Load Datasets from Kaggle:
1. Go to [Kaggle](kaggle.com) and your profile.
2. Go to Setting -> API -> Expire Token
3. Click on *Create New Token* and check downloads for Kaggle.json file.
4. Open Colaboratory Notebook and Upload the Kaggle.json in the environment.
5. Run the following code in first few cells and refresh the folder:
<code>
!pip install -q kaggle
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 /root/.kaggle/kaggle.json
!kaggle datasets download -d user/dataset
!unzip /content/dataset.zip
</code>

### References:
[StackOverFlow Answer](https://stackoverflow.com/questions/49310470/using-kaggle-datasets-in-google-colab#:~:text=Upload%20your%20kaggle.json%20file%20using%20the%20following%20snippet,be%20located%3A%20%21mkdir%20-p%20~%2F.kaggle%20%21cp%20kaggle.json%20~%2F.kaggle%2F)
