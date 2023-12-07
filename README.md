# Diabetes Prediction Project

This project is designed to predict diabetes using machine learning models and data visualization techniques. The project consists of five main components:

Machine Learning Models: The project uses two machine learning models - Linear Regression and Random Forest for predictions.  
Data Visualization: The project includes code that generates a heatmap to visualize the dataset and understand the relationship between the features.  
Web Interface: An HTML file is used to control the layout and appearance of the website and structure the web page.  
Website: A file named “Website.py" which runs the website locally using flask and incorporates the model through a h5 file   
h5 File: A h5 created when running either model; used so that the website can interact with the model

## **Required Packages**
The following packages are required to run the models and the website:
Flask
Numpy
TensorFlow
Matplotlib
Scikit-Learn (sklearn)
Pandas
Seaborn

pip install flask numpy tensorflow matplotlib sklearn pandas seaborn
![image.png](attachment:6838b2bc-00e6-4f2e-81de-2fcc4c1bd7d1.png)


## **Instructions to run the website locally**
1. Download the required "Website.py", html file, and desired model (either RandomForrest.py or LinearRegression.py)
3. Run the desired model. This will create an h5 file, which the website uses to predict diabetes. Skip this step if you have decided to use the included h5 file, which was obtained through the our best model (random forrest). 
4. Run "Website.py" and click the IP address that is generated and running on your local machine (terminal) 
   ![image.png](attachment:19d6b552-66f4-48a2-94af-875124acbd1c.png)
5. Fill out the form  
   ![image.png](attachment:5b2ee1fa-9d50-4c5d-8d48-916709942efe.png)
6. Click Submit after filling out the form. After submitting the form, the outcome will be displayed below the *submit* button
   ![image.png](attachment:00dc8410-ace0-4ca6-b83c-99e7846259f3.png)


 
