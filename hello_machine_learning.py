# install anaconda
# run jupiter by running Jupyter Notebook (Anaconda3) application
# or in terminal jupiter notebook
# this will start a jupiter server in localhost:8888
# run this server on web browser and make new runbook for python 3
# change the title of the notebook to HelloWorld
# download dataset from https://www.kaggle.com
# import pandas as pd to jupyter
# then to import the dataset we downloaded from kaggle.com. insert the commands to jupiter
# import pandas as pd
# dataset = pd.read_csv('vgsales.csv')
# dataset
# and than all the data will be present on jupiter server

import pandas as pd
from  sklearn.tree import  DecisionTreeClassifier
music_data = pd.read_csv(music.csv)
X = musice_data.drop(columns=['genre'])
Y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X, Y)
model.predict([[21,1],22,0])
# and the program will predict that 21 year old male will most likely like HipHop
# and girls 22 years old will most likely like Dance music
# it's not a good platform to document anaconda+jupyter :/
