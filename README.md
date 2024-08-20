# End to End Machine Learning Project

## Student Performance Indicator
#### Introduction About the Data :
##### Problem Statement
The objective of this project is to investigate how various factors influence student performance (test scores). We will explore the relationship between test scores and the following variables:

1. Gender: Analyze whether there are gender-based differences in performance.
2. Ethnicity: Investigate how ethnicity impacts test scores.
3. Parental Level of Education: Explore correlations between parents’ education levels and student performance.
4. Lunch: Examine whether the type of lunch (standard or free/reduced) affects test scores.
5. Test Preparation Course: Understand the impact of completing a test preparation course on student outcomes.

##### Dataset Information
The dataset includes the following columns:

  - Gender: Sex of students (Male/Female)
  - Race/Ethnicity: Ethnicity of students (Group A, B, C, D, E)
  - Parental Level of Education: Parents’ final education (Bachelor’s degree, Some college, Master’s degree, Associate’s degree, High school)
  - Lunch: Type of lunch (Standard or Free/Reduced)
  - Test Preparation Course: Whether the test preparation course was completed or not
  - Math Score
  - Reading Score
  - Writing Score

Dataset Source Link :  https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977

The data consists of 8 column and 1000 rows.

### Approach for the project
1. Data Ingestion :

    - In Data Ingestion phase the data is first read as csv.
    - Then the data is split into training and testing and saved as csv file.

2. Data Transformation :

    - In this phase a ColumnTransformer Pipeline is created.
    - For Numeric Variables , then Standard Scaling is performed on numeric data.
    - for Categorical Variables one hot encoding performed , after this data is scaled with Standard Scaler.
    - This preprocessor is saved as pickle file.

3. Model Training :

    - In this phase base model is tested . The best model found was linear regression.
    - This model is saved as pickle file.

4. Prediction Pipeline :

    - This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation :

    - Flask app is created with User Interface to predict the math score inside a Web Application.
  

      ![Screenshot 2024-08-20 220514](https://github.com/user-attachments/assets/13596ee2-95e9-46ca-af7c-e351bd5fbc80)











