## e-commerce Fraud Detection Study

### Model
  * EDA, feature selection
      * We engineered a number of new features to train our model on -- for a feature engineering discussion, read more here: [Feature Engineering](https://github.com/jpcenteno80/fraud_detection/feature_engineering.md)
      * We identified a column in the data that presented a potential leakage issue -- payout_type.  A payout type indicates that a payment has been made.  If a payment hasn't been made, that means that the event may have been identified as fraudulent by the company.  (Update: after further investigation we determined this feature had little impact on model score)
  * Initial model testing
      * random forest, ada boost.
      * start with few, strong features
      * as feature exploration progresses, add more features to model
  * Metrics for model success
      * recall: ability for model to find all fraud samples
      * precision: from all true fraud cases, ability to correctly label them as fraud
  * Prediction framework: pickle model and get script ready for web app

### Database
  * MongoDB database to store each example the model predicts on

### Web App
  * Flask: app in server will receive live requests and make a prediction that will be saved in the MongoDB database

### Github Repo
  * Web app will be stored in github repo

### AWS Deployment
  * Web site with classification engine will be edployed to an AWS server

### Future Work
  * In depth feature exploration
      * 'ticket_types': extract total cost from embedded dictionary
      * 'email_domain': explore prediction significance of gmail, yahoo, hotmail, (edu/org/gov) types of accounts
      * 'description': use NLP to explore url description keywords associated with fraud
  * Model score visualization and success metrics:
      * ROC curve
      * cost of fraud: missed fraud times the cost of the fraud

### Model Framework

![Alt text](https://github.com/jpcenteno80/fraud_detection/blob/master/images/flowchart.png)
