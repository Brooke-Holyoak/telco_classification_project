
# Telco Dataset Customer Churn Classification Project


****
## Project Goals:
    -Acquire Data: from a SQL database, create an acquire.py module with necessary functions
    -Clean data and create a prepare.py module with necessary functions
        -ie: look at null-values and either drop or impute values or rows where appropriate.
        -assign scalar values to columns containing strings to allow modeling to work

****
#### Business Goals
> - Construct a ML classification model that accurately predicts what features are drivers in Telco Customer Churn.
> - Document process well enough to be presented or understood while reading.

****
## Initial Hypotheses:
    - Payment_type is a driver and correlated with churn

    - Having multiple lines is a driver and correlated with churn

    - Internet_type is a driver and correlated with churn
    
**** 



#### Audience
> - Codeup Data Science students

#### Project Deliverables
> - A final report notebook 
> - A final report notebook presentation
> - All necessary modules to make my project reproducible

#### Project Context
> - The Telco dataset I'm using came from the Codeup SQL database.


****
## Data Dictionary:
    
> ### Summary: 7043 observations(rows), Each observation represents a single customer with 21 variables

**CustomerID**: A unique ID that identifies each customer.

**Gender**: The customer’s gender: Male, Female

**Senior Citizen**: Indicates if the customer is 65 or older: Yes, No

**Partner**: Indicate if the customer has a partner: Yes, No

**Dependents**: Indicates if the customer lives with any dependents: Yes, No. Dependents could be children, parents, grandparents, etc.

**Tenure Months**: Indicates the total amount of months that the customer has been with the company by the end of the quarter specified above.

**Phone Service**: Indicates if the customer subscribes to home phone service with the company: Yes, No

**Multiple Lines**: Indicates if the customer subscribes to multiple telephone lines with the company: Yes, No

**Internet Service**: Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic, Cable.

**Online Security**: Indicates if the customer subscribes to an additional online security service provided by the company: Yes, No

**Online Backup**: Indicates if the customer subscribes to an additional online backup service provided by the company: Yes, No

**Device Protection**: Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company: Yes, No

**Tech Support**: Indicates if the customer subscribes to an additional technical support plan from the company with reduced wait times: Yes, No

**Streaming TV**: Indicates if the customer uses their Internet service to stream television programing from a third party provider: Yes, No. The company does not charge an additional fee for this service.

**Streaming Movies**: Indicates if the customer uses their Internet service to stream movies from a third party provider: Yes, No. The company does not charge an additional fee for this service.

**Contract**: Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year.

**Paperless Billing**: Indicates if the customer has chosen paperless billing: Yes, No

**Payment Method**: Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check

**Monthly Charge**: Indicates the customer’s current total monthly charge for all their services from the company.

**Total Charges**: Indicates the customer’s total charges, calculated to the end of the quarter specified above.

**Churn Label**: Yes = the customer left the company this quarter. No = the customer remained with the company. Directly related to Churn Value.

****
## Executive Summary - Conclusions & Next Steps

> - I found that all of the classification models I created performed better than my baseline prediction of 73%. 
> - I chose the Random Forest model as my best model with a 89% accuracy rate for predicting my target value, Churn_Yes. This model outperformed my baseline score of 73% accuracy, so it has value.
> - Some initial exploration and statistical testing revealed that further exploration of tenure, monthly charges and total charges might help my models predict with even more accuracy, and with more time, I would like to further explore those features.

****
### Plan
- (Using Faith Kane's streamlined process in her Iris Classification project, I will proceed with the following plan- minor changes to adjust for the Telco Dataset)
- [x] Create README.md with data dictionary, project and business goals, and initial hypotheses.
- [x] Acquire data from the Codeup SQL Database and create a an acquire.py module.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x]  Clearly define hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models.
- [x] Choose the model with that performs the best and evaluate that single model.
- [x] Create csv file with the measurement id, the probability of the target values, and the model's prediction for each observation in my test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

****
### Reproduce this project:
- You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook