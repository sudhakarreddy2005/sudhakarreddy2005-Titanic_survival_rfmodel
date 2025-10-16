# Titanic Survival Prediction App

## Overview  
This project focuses on predicting the likelihood of passenger survival on the Titanic using a **Machine Learning model (Random Forest Classifier)**.  
It combines **data analysis, feature engineering, and visualisation** in Python with an **interactive web application** built using Streamlit.  

The application allows users to experiment with passenger attributes and instantly view survival predictions, showcasing how Machine Learning models can be deployed in real-world decision-making scenarios.  


## Live Application  
Access the deployed web app here:  
[**Titanic Survival Prediction App**](https://sudhakarreddy2005-titanicsurvivalrfmodel-1610.streamlit.app/)



## GitHub Repository  
[**sudhakarreddy2005-Titanic_survival_rfmodel**](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel)



## Machine Learning Model Details  
- **Algorithm:** RandomForestClassifier  
- **Library:** scikit-learn  
- **Target Variable:** `Survived` (0 = Did Not Survive, 1 = Survived)  
- **Input Features:**  
  `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`  

The model was trained on the historical Titanic dataset to identify relationships between socio-demographic and travel attributes and survival outcomes. Random Forest was chosen for its robustness, interpretability, and strong performance on tabular data.



## Streamlit Application Overview  

The **Titanic Survival Prediction App** is an **interactive Machine Learning-powered web interface** that allows users to simulate survival predictions by adjusting passenger attributes.  

### Purpose  
The app demonstrates how a trained Machine Learning model can be integrated into a web-based interface to provide real-time predictive insights, bridging the gap between data science experimentation and accessible, user-facing tools.

### Functionality  
Users can modify key features—such as passenger class, gender, age, and fare—and instantly receive a prediction on whether the passenger would have survived. The app’s prediction engine runs on the trained **Random Forest model** (`RFclassifier_titanic_ml.joblib`).

**User Inputs:**  
- Passenger Class (1 / 2 / 3)  
- Sex (Male / Female)  
- Age  
- Number of Siblings/Spouses aboard (SibSp)  
- Number of Parents/Children aboard (Parch)  
- Fare  

**Output:**  
- *Survived* or *Did Not Survive*  

The prediction result is generated live within the Streamlit interface, enabling users to explore the model’s behaviour interactively.



## Application Interface  

Below is a placeholder for an image of the deployed application.  
Replace this with a screenshot of your Streamlit interface (for example, `app_interface.png`).

![Application Interface](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel/blob/main/app.png)



## Visualisations and Insights  

### 1. Dataset Overview  
![Dataset Overview](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel/blob/main/datasetoverview.png)  
An overview of the dataset highlighting key variables and data completeness.

### 2. Missing Value Heatmap  
![Missing Values](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel/blob/main/nullvaluesheatmap.png)  
A heatmap visualising missing values guided the data cleaning process, revealing gaps in `Age` and `Embarked`.

### 3. Survival by Gender  
![Survival by Gender](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel/blob/main/gendersurvuval.png)  
Female passengers exhibited a substantially higher survival rate, confirming gender as a significant feature.

### 4. Survival by Passenger Class  
![Survival by Class](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel/blob/main/pclass%20survival.png)  
First-class passengers had the highest survival rate, suggesting socio-economic status influenced rescue priority.

### 5. Age Distribution and Survival  
![Age Distribution](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel/blob/main/age%20survival.png)  
Younger passengers were more likely to survive, indicating potential prioritisation during evacuation.

### 6. Embarktown and Survival Relationship  
![Embarktown vs Survival](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel/blob/main/town%20survuval.png)  
The passengers going to cherbourg are likely  survived than other towns

### 7. Correlation Heatmap  
![Correlation Heatmap](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel/blob/main/heatmap%20matrix.png)  
A heatmap of confusion matrix of the Machine Learning model

### 8. Accuracy Importance (Random Forest)  
![Feature Importance](https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel/blob/main/accuracy%20rf%20chart.png)  
The Random Forest model determined that maximum accuracy is 80.597



## Running the Application Locally  

```bash
git clone https://github.com/sudhakarreddy2005/sudhakarreddy2005-Titanic_survival_rfmodel.git
cd sudhakarreddy2005-Titanic_survival_rfmodel
pip install -r requirements.txt
streamlit run titanic_ml_app.py
