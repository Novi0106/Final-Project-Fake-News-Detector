<h1 align="center"> Final-Project-Fake-News-Detector </h1>
<p align="center">
  <img src="https://media.giphy.com/media/n2IPMYMthV0m4/giphy.gif" />
</p>

<p align="center">
  <i>
Andre Novikov - Data Analysis May21 Cohort
  </i>
</p>

<h2 align="center"> Content </h2>

- [Project Description](https://github.com/Novi0106/Final-Project-Fake-News-Detector/edit/main/README.md#project-description)
- [Dataset](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#dataset)
- [Approach](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#approach)
- [Key Learnings](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#key-learnings)
- [Repository Structure](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#repository-structure)
- [How to run the tool?](https://github.com/Novi0106/Happiness-Team/blob/main/README.md#how-to-run-the-tool?)

  
<h2 align="center"> Project Description </h2>
<p align="center">
The goal of this project is to build a tool that is able to classify a news article as being either fake or real.
For the purpose of this project we will clasify real or fake on a boolean basis and not as a float value. We will do this by training a model using set
of labelled data in both English and German. We will consider those news to be fake that are published by sources that are well known for publishing misleading information, since we cannot rely on a full fact check (or rather don't have the technical knowledge to automize it yet).
</p>

<h2 align="center"> Dataset </h2>
<p align="center">
The dataset consists of labelled articles from multiple source:
  <ol type = "1" >
         <li>4,230 German articles, scraped over 4 days using the Newscather API wrapper and BeautifulSoup and labelled based on news source</li>
         <li>44,185 labelled English articles from the  <a href="https://www.uvic.ca/engineering/ece/isot/datasets/fake-news/index.php">University of Victoria</a></li>
         <li>3,988 articles from a <a href="https://www.kaggle.com/jruvika/fake-news-detection">Kaggle Dataset</a> complemented with scraped German data to serve as an independent dataset to test the model we train</li>
  </ol>
</p>

<h2 align="center"> Approach </h2>
<p align="center">
Apart from the data scraping an cleaning we will use the sklearn tfidf vectorizer to encode the string data. TF (or term frequency) stands for the frequency of a word within a given document (or in this case a news article), while idf (or inverse document frequency) stands for a word's frequency across all documents (or all news articles). On basis of these two values the encoder quantifies a term's importance. This is the tool that helps to build a vocabulary for our model.
</p>

<p align="center">
We then use the encoded data to feed into sklearn's PassiveAggresiveClassifier which essentially takes each example sequentially (instead of a batch) and then does one of two things:
<ol type = "1" >
         <li>If the classification is correct the model stays "Passive" and does not change </li>
         <li>If the classification is incorrect it becomes "Aggressive" and changes the model </a></li>
  </ol>
</p>

<p align="center">
  <img src= /5.%20Images/approach.png /> <br>
  <i> Chosen Approach </i>
</p>


<h2 align="center"> Key Learnings </h2>
<p align="center">
Initially the idea was to use the labeled data to either used logistics regression or go down the Naive Bayes Classifiers to predict the label of a news article. However, a PassiveAggresive classifier seemed more powerful in this case (especially considering the ease of setting it up), but it would be still interesting to see whether other machine learning algorithms could serve for the model. Especially, because the mathematical logic behind the PassiveAggressive classifier was close to impossible to understand without a strong foundation in math.
</p>
<p align="center">
Scraping German data was really a challenge, especially because fake news websites are all structured in vastly different ways with no API wrapper to scrape them. Ideally, more time for data collection could serve well to improve the the models accuracy for German news.
</p>
<p align="center"> 
While the accuracy score for independent data is still strong, it would be extremely helpful to understand the right composition for the dataset a bit better, especially with respect to different writing styles. Ideally, that would mean to have a manually labelled dataset that was made on basis of an actual fact check similar to Politifacts.com.
</p>

<h2 align="center"> How to run the tool? </h2>

<ol>
  <li>pip install streamlit via your terminal in an environment of your choice./li>
  <li>Download the files in <a href="https://github.com/Novi0106/Final-Project-Fake-News-Detector/tree/main/4.%20Final%20tool ">this folder</a>.</li>
  <li>Via your terminal navigate to the directory where the files are stored via the terminal and enter "streamlit run App.py".
</p></li>
  <li>This should trigger a UI to open via localhost that you can use to play with the tool using free text or .txt files.</li>
</ol>
