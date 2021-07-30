#!/usr/bin/env python
# coding: utf-8
# %%

# %%
def process_inputs(text):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import pandas as pd
    import re
    
    german_stop_words = stopwords.words('german')
    english_stop_words = stopwords.words('english')
    
    news = ["".join(text)]
    news = pd.DataFrame(news, columns=['content'])
    
    news['content'] = news['content'].str.split(' ').apply(lambda content:
    ' '.join([word for word in content if word not in english_stop_words]))
    
    news['content'] = news['content'].str.split(' ').apply(lambda content:
    ' '.join([word for word in content if word not in german_stop_words]))
    
    news['content'] = news['content'].replace(r'\n',' ', regex=True)
    
    return news


# %%
def news_classification(news):
    import pandas as pd
    import numpy as np

    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import PassiveAggressiveClassifier
    
    news = news['content']
    complete_news = pd.read_csv('complete_news_clean.csv')
    
    label_converter = {1:'Real', 0:'Fake'}
    complete_news = complete_news.replace({'label' : label_converter})
    
    X = complete_news['content']
    y = complete_news['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 40)
    
    tfidf = TfidfVectorizer(max_df = 0.85)
    
    
    tfidf_train = tfidf.fit_transform(X_train.astype('U')) 
    tfidf_test = tfidf.transform(X_test.astype('U'))
    
    model = PassiveAggressiveClassifier(max_iter = 150, shuffle = True)
    model.fit(tfidf_train,y_train)
    
    #check your news against the model
    
    tfidf_test = tfidf.transform(news.astype('U'))
    
    y_pred = model.predict(tfidf_test)[0]
    
    
    classification = y_pred
    
    return classification


# %%
# Initial wrapper to have a separate function to classify seperately from setting up the model
# This is merely to refactor the solution in the future and make it a bit more modular
# For now this function is not relevant

def classify_news(news):
    import pandas as pd
    import numpy as np

    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import PassiveAggressiveClassifier
    
    news = news['content']
    tfidf, model = setup_baseline_model()
    
    tfidf_test = tfidf.transform(news.astype('U'))
    
    y_pred = model.predict(tfidf_test)[0]
    
    
    print(f'Those news look like they are {y_pred}')


# %%
# Initially the plan was to have a separate function for csv processing
# However this was not very compatible with streamlit, so this remains for other use cases

def process_csv(file):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import pandas as pd
    import re
    
    german_stop_words = stopwords.words('german')
    english_stop_words = stopwords.words('english')
    
    news = ["".join(open(file).readlines())]
    news = pd.DataFrame(news, columns=['content'])
    
    news['content'] = news['content'].str.split(' ').apply(lambda content:
    ' '.join([word for word in content if word not in english_stop_words]))
    
    news['content'] = news['content'].str.split(' ').apply(lambda content:
    ' '.join([word for word in content if word not in german_stop_words]))
    
    news['content'] = news['content'].replace(r'\n',' ', regex=True)
    
    return news
