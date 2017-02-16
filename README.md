## e-commerce Fraud Detection Study

### Model
  * EDA, feature selection
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
