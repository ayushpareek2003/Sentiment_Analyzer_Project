# Sentiment_Analyzer_Project
Group Members

22BDS011 (Ayush Pareek), 22BDS058 (Suyash Suryavansh), 22BDS030 (Jatin Kushwaha), 22BDS057 (Teena Chowdary), 22BDS034 (Lalit Yadav), 22BDS027 (Hitesh Sharma)

How to use:

First your input tweet must be pre-processed using the function "Pre_process" implemented in the python script "support.py". After this you have to load our trained model named "T_M.h5"
 
use "model.predict([input array you get after preprocessing your data using the mentioned function])"

Size of trained model is approx 450MB, so we can't upload it on github (Gdrive link is provided below)

Then you have to use another function "decode_sentiment" available in "support.py" using that function you will get the final output as 1 for positive feeling and 0 for negative.

dont forgot to add "globe_6B_300.txt" file with support.py python file.

Links:

Model = https://drive.google.com/file/d/1vUm11Bp4YRUZEuHpQpjmIN2M85CTWcXg/view?usp=sharing

globe_6B_300.txt = https://www.kaggle.com/datasets/thanakomsn/glove6b300dtxt 


 
