## Feature Engineering

This page discusses our feature engineering process

### Features Created:
* Label (fraud or not)
* Total cost
* Potential cost
* Time to event
* Email domain


### Label
There were a number of different account_types that indicated potential fraud.  We decided to label every account type that was not Premium as potentially fraudulent.

### Total Cost and Potential Cost
After reading through the ticket_types column, we decided to create two new features:
* Total Cost - sales quantity * cost per ticket
* Potential Cost - available quantity * cost per ticket

These ended up being two of the most important features *(Total Cost being the most important)* to our Random Forest Classifier

![Feature Importances](/images/loo.png)

### Time to Event
We found the time between when the event was created to the scheduled start time of the event, was a good indicator of fraud.  In the graph below it is clear that fraudulent events have a much shorter time lag.  It seems fraudsters are predictably impatient.

![Time to event](/images/days_since_created.png)

### Email Domain
We found that fraud was much more likely among events that registered with a public email domain (i.e. @yahoo.com, @hotmail.com, etc.).  We created a list of known public domain names and classified each event as having a public domain name or not.
![Email domain](/images/email_domain.png)
