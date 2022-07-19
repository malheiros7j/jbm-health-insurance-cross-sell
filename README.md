# Insurance All Company - Health Insurance Cross Sell

The following context is completely fictitious, the company, the context and the CEO. The business questions are also fictional but were made in an attempt to exemplify how they would be required in a business work environment.

## The Context

Insurance All is a company that provides health insurance to its customers. The product’s team is analyzing the possibility of offering a new product to the insurance customer: auto insurance. Like health insurance, the customers of this new auto insurance plan need to pay an amount annually to Insurance All to obtain an amount insured by the company, intended for the costs of an eventual accident or damage to the vehicle.

Insurance All surveyed nearly 380.000 customers about their interest in acquiring the new product , the auto insurance. All the clients showed interest or not in purchasing auto insurance and these responses were saved in a database along with other customer attributes.

The product team selected 127.000 new customers who didn’t respond to the survey to participate in a campaign, in which they will be offered the new auto insurance product. The offer will be made by the sales team through phone call. 

**However, the sales team only has the capability to make 20.000 calls within the campaign duration.***


## The Challenge

In that context, you were hired as a Data Scientist Consultant to build a model that predicts if the cliente would be interested or not in purchasing the new auto insurance. With your solution, the sales team expect to prioritize the customers with more propense in obtaining the new product and, thus, optimize the campaign by making only contacts with customers most likely to purchase.

As a result of your consultancy, you will need to deliver a report containing some analysis and answers to the following questions:

- Main Insights of the most relevant attributes of the customers that are interested in purchasing auto insurance.

- What percentage of customers' interest in purchasing auto insurance will the sales team be able to reach by making 20.000 calls?

- If the sales team’s capacity increases to 40.00 calls, what would be the percentage of people interested in purchasing a new auto insurance the sales team would be able to reach out.

- How many calls does the sales team need to make contact to 80% of the customers interested in purchasing auto insurance?

## The Dataset

The dataset is located in an AWS environment where the customer database and their information are located. To extract these data, SQL queries were used to organize the data for the project solution. Each row represents a customer and each columns contains some attributes that describe that customer, in addition to their survey response, in which they mentioned their interest or not in purchasing the new insurance product.

The attributes of each customer can be described by:

* **Id**  unique customer identifier.
* **Gender** - customer's gender.
* **Age** - customer's age.
* **Driving License** - 0, the customer does not have a driving license and 1, the customer has driving license.
* **Region Code** - Customer's region code.
* **Previously Insured** - 0, the customer does not have auto insurance and 1, the customer already has auto insurance.
* **Vehicle Age** - vehicle age.
* **Vehicle Damage** - 0, customer has never had his vehicle damaged in the past and 1, customer has had his vehicle damaged in the past.
* **Annual Premium** - amount the customer paid the company for annual health insurance.
* **Policy sales channel** - anonymous code for the customer contact channel.
* **Vintage** - number of days that the customer was associated with the company through the purchase of health insurance.
* **Response** - 0, the customer is not interested and 1, the customer is interested.

## Solution Planing

#### What is the solution and how it will be delivered?
The development of a machine learning model that ranks the customers based in his probability (propensity score) to purchase the new auto insurance. 

The Final Model will be available in an API, and may be used by the Company in any time needed.

#### Hosting 
The model will be hosted in a Heroku Environment and is available in the url: https://health-insurance-jbm.herokuapp.com/

#### Delivery Method and Google Sheets  
A script was developed in Google Sheets in which the input data are the attributes and information of the customers, and when executing the script it queries the model in the Heroku environment and returns the probability of the customer to acquire the new auto insurance.

The Google Sheets Spreadshet its located at: https://docs.google.com/spreadsheets/d/164sfg8vRjYGQ_k-3QX85D-L4Pf6gdf-alpOwOTJpJcY/edit?usp=sharing

### Final Planing

* [1. Description and Business Problem ](#1-description-and-business-problem)
* [2. Database and Business Assumptions](#2-database-and-business-assumptions)
* [3. Solution Strategy ](#3-solution-strategy)
* [4. Exploration Data Analysis](#4-exploration-data-analysis)
* [5. Machine Learning Model Selection](#5-machine-learning-model-selection)
* [6. Model Performance ](#6-model-performance)
* [7. Business Results](#7-business-results)
* [8. Model in Production ](#8-model-in-production)
* [9. Conclusion](#9-conclusion)
* [10. Learning and Future Work](#10-learning-and-future-work)


# 1. Description and Business Problem


# 2. Database and Business Assumptions


# 3. Solution Strategy 


# 4. Exploration Data Analysis


# 5. Machine Learning Model Selection


# 6. Model Performance


# 7. Business Results


# 8. Model in Production


# 9. Conclusion


# 10. Learning and Future Work



