## e-commerce Fraud Detection Study

### Model
  * EDA, feature selection
      * We engineered a number of new features to train our model on -- for a feature engineering discussion, read more here: [Feature Engineering](/feature_engineering.md)
      * We identified a column in the data that presented a potential leakage issue -- payout_type.  A payout type indicates that a payment has been made.  If a payment hasn't been made, that means that the event may have been identified as fraudulent by the company.  (Update: after further investigation we determined this feature had little impact on model score)
  * Initial model testing
      * random forest, ada boost.
      * start with few, strong features
      * as feature exploration progresses, add more features to model
  * Metrics for model success
      * Recall: ability for model to find all fraud samples
      * Precision: from all true fraud cases, ability to correctly label them as fraud
      * We chose recall to be our primary metric and precision to be our secondary metric.  We made our metric choices to prioritize catching as much fraud as possible over potentially inconveniencing legitimate users.  However, we still kept these inconveniences in mind when selecting our final model.
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
      * NLP on event name
  * Model score visualization and success metrics:
      * ROC curve
      * cost of fraud: missed fraud times the cost of the fraud
  * Train a neural network on the dataset
      * Given more time, we would like to explore using a neural network to predict fraudulent events


### Model Framework
We extracted and analyzed the text from our description column using the combination of a Term-frequency Inverse-document-frequency model and a Gaussian Naive Bayes model.  We generated fraud or not predictions based on this model, then added those predictions as a column to the rest of our feature matrix.

Once our feature matrix was complete, we used a Random Forest Classifier to make our final fraud prediction.

![Alt text](https://github.com/jpcenteno80/fraud_detection/blob/master/images/flowchart.png)

### Web App Framework

![Alt text](/images/web_app_flow.png)
