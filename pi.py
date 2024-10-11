import mpmath
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Calculate pi to 10,000 digits
mpmath.mp.dps=10000
pi=str(mpmath.pi)[2:]

# Feature vector is index of digit
x=list(range(len(pi)))
x=np.array(x).reshape(-1,1)

# Target vector is whether the digit is 0,1,2,3,4 or 5,6,7,8,9
y=[int(d)>4 for d in pi]
print("Expected probability "+str(y.count(0)/len(y)))

# z tracks the running accuracy of the model
z=0
for i in range(1000):
    # Split data into train and test sets
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

    # Build Random Forest Classifier
    clf=RandomForestClassifier()
    clf.fit(x_train,y_train)

    # Get predictions
    y_pred=clf.predict(np.array(x_test).reshape(-1,1))

    # Score predictions
    score=0
    for yp,yt in zip(y_pred,y_test):
        if yp!=yt: # The classifier predicts wrong, but this is still good
            score+=1

    # Update running accuracy
    z+=(score/len(y_test))
    print("Prediction accuracy after "+str(i+1)+" iterations: "+str(z/(i+1)))

