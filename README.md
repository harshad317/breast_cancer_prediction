# Breast Cancer Prediction

According to the world health organization  (WHO)  Breast  cancer  is  the  most  frequent cancer  among  women,  impacting  2.1  million women each year, and also causes the greatest number of cancer- related deaths among women. In 2018, it is estimated that 627,000 women died from breast cancer – that is approximately 15%  of all cancer deaths among  women. While  breast  cancer  rates  are  higher  among  women  in more  developed  regions,  rates  are  increasing  in  nearly every region globally. In order to improve breast cancer outcomes and  survival, early  detection is critical. There are two early detection strategies for breast cancer: early diagnosis  and  screening.  Limited  resource  settings  with weak  health  systems  where  the  majority  of  women  are diagnosed in late stages should prioritize early diagnosis programs based on awareness of early signs and symptoms and prompt referral to diagnosis and treatment.  Early  diagnosis  strategies  focus  on  providing timely access to cancer treatment by reducing barriers to care and/or improving access to effective diagnosis services. The goal is to increase the proportion  of breast cancers  identified  at  an  early  stage,  allowing  for  more effective  treatment  to  be  used  and  reducing  the  risks  of death from breast cancer. Since early detection of cancer is  key  to  effective  treatment  of  breast  cancer  we  use various  **machine  learning  algorithms  to  predict  if  a tumor  is  benign  or  malignant,  based  on  the  features provided by the data.**

Breast cancer (BC) is one  of  the  most common cancers among  women  worldwide,  representing  the  majority  of new cancer cases and cancer-related deaths according to global  statistics,  making  it  a  significant  public  health problem in today’s society. The early diagnosis of BC can improve the prognosis and chance of survival significantly, as it can promote timely clinical treatment to patients. Further accurate classification of benign tumors can prevent patients undergoing  unnecessary  treatments.  Thus,  the  correct diagnosis of BC and classification of patients into malignant or benign groups is the subject of much research. Because of its unique advantages in critical features  detection  from  complex  BC  datasets,  machine learning (ML) is widely recognized as the  methodology of choice in BC pattern classification and forecast modeling. 
 
## Some Risk Factors for Breast Cancer:
 The  following  are  some  of  the  known  risk  factors  for breast  cancer.  However,  most  cases  of  breast  cancer cannot be linked to a specific cause. Talk to your doctor about your specific risk. 
 
1. **Age.**  The  chance  of  getting  breast  cancer  increases  as women  age.  Nearly  80  percent  of  breast  cancers  are found in women over the age of 50. 
 
2. **Personal  history  of  breast  cancer.**  A  woman  who  has had breast cancer in one breast is at an increased risk of developing cancer in her other breast. 
 
3. **Family history of breast cancer.** A woman has a higher risk of breast cancer if her mother, sister or daughter had breast  cancer,  especially  at  a  young  age  (before  40). Having  other relatives  with breast  cancer may also raise the risk. 

4. **Genetic factors.** Women with certain genetic mutations, including changes to the BRCA1 and BRCA2 genes, are at  higher  risk  of  developing  breast  cancer  during  their lifetime. Other gene changes may raise breast cancer risk as well. 
 
5. **Childbearing and menstrual history.** The older a woman is when she has her first child, the greater her risk of breast cancer. 
 
Also at higher risk are: 
 
1. Women who menstruate for the first time at an early  
        age (before 12) 
 
2. Women who go through menopause late (after age   
        55) 
 
3. Women who’ve never had children 


## Role of Machine Learning In Detection of Breast Cancer 
 
A mammogram is an x-ray picture of the breast. It can be used  to  check  for  breast  cancer  in  women  who  have  no signs  or  symptoms  of  the  disease.  It  can  also  be used  if you have a lump or other sign of breast  cancer. Screening mammography is the type of mammogram that checks  you  when  you  have  no  symptoms.  It  can  help reduce  the  number  of  deaths  from  breast  cancer  among women  ages  40  to  70.  But  it  can  also  have  drawbacks. 
Mammograms can sometimes find something that looks abnormal but isn't cancer. This leads to further testing and can  cause  you  anxiety.  Sometimes  mammograms  can 
miss  cancer  when  it  is  there.  It  also  exposes  you  to radiation. You  should talk to your  doctor  about the benefits and drawbacks of mammograms. Together, you can decide when to start and how often to have a mammogram. Now  while  its  difficult  to  figure  out  for  physicians  by seeing  only  images  of  x-ray  that  weather  the  tumor  is toxic or not training a machine learning model according to the identification of tumour can be of great help.

## Tech Stack:
* Front-End:HTML, CSS
* Back-End:Flask
* IDE:Jupyter Notebook, Visual Studio Code

## How to run this app:
* First create a virtual environment by using this command: conda create -n myenv python=3.6
* Activate the environment using the below command: conda activate myenv
* Then install all the packages by using the following command: pip install -r requirements.txt
* Now for the final step. Run the app
* python app.py

## Data Preprocessing:
* Categorical columns like **diagnosis** has been imputed using the mapping method.
* Numerical columns such as **radius_se, perimeter_se, area_se, smoothness_se, fractal_dimension_se** has high skewness and they has been transformed using numpy.log1p for better use of the column.

## Model Creation:
* Different types of models were tried like catboost, random forest, logistic regression, xgboost, support vector machines, knn, naive bayes.
* Out of these catboost, xgboost and lgbm were top 3.
* The conclusion were made using classification metric **f1_score**.

## Model Deployment:
The model is deployed using Flask at Heroku server.


## Problem statement
Breast  Cancer  is  one  of  the  leading  cancer developed  in many  countries  including  India.  Though  the  endurance rate  is  high  –  with  early  diagnosis  97%  women  can survive for more than 5 years. Statistically, the death toll due  to  this  disease  has  increased  drastically  in  last  few decades.  The  main  issue  pertaining  to  its  cure  is  early recognition. Hence, apart from medicinal solutions some Data Science solution needs to be integrated for resolving 
the death causing issue. This  analysis  aims  to  observe  which  features  are  most helpful  in  predicting  malignant  or  benign  cancer  and  to see general trends that may aid us in model selection and hyper parameter selection. The goal is to classify whether the breast cancer is benign or malignant. To achieve this 
i have used machine learning classification methods to fit a function that can predict the discrete class of new input. 

## Screenshots:

### Front page:
![front_page](https://user-images.githubusercontent.com/15306703/155070115-7ecd228c-9c7c-4e9d-8a54-93d2f9bf80a7.png)

### Prediction page:
![predictor](https://user-images.githubusercontent.com/15306703/155070321-9095288e-54f1-4093-8920-d7f6fbfcc05b.png)

## Final prediction:
**1. If Malignant**
![malignant_1](https://user-images.githubusercontent.com/15306703/155070929-41aa1b5a-498b-4bb0-89e3-0629fbe861ff.png)
![malignant_2](https://user-images.githubusercontent.com/15306703/155070932-196b7699-ee8e-4cb3-9171-7c1904d04c2b.png)
![malignant_3](https://user-images.githubusercontent.com/15306703/155070938-136d4a43-4094-46c7-8fa8-6fe10f695470.png)

**2. If Benign**
![benign](https://user-images.githubusercontent.com/15306703/155071297-7a593861-c362-4c97-b561-4aac844ae960.png)


## Conclusion
In this project in python, we learned to build a breast cancer  tumour  predictor  on  the  wisconsin  dataset and  created  graphs  and  results  for  the  same.  It  has been  observed  that  a  good  dataset  provides  better accuracy.  Selection  of  appropriate  algorithms  with good  home  dataset  will  lead  to  the  development  of prediction systems. These systems can assist in proper  treatment  methods  for  a  patient  diagnosed with breast cancer. There are many treatments  for a patient based on breast cancer stage; data mining and machine learning can be a very good help in deciding  the  line  of  treatment  to  be  followed  by 
extracting knowledge from such suitable databases.
