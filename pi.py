import mpmath
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from tqdm import tqdm

mpmath.mp.dps=10000
pi=str(mpmath.pi)[2:]

x=list(range(len(pi)))
x=np.array(x).reshape(-1,1)
y=[d in "01234" for d in pi]
print(y.count(0)/len(y))

# z tracks the running accuracy of the model
z=0
for i in range(1000):
    # Split data into train and test sets
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

    # Build Random Forest Classifier
    clf=RandomForestClassifier()
    clf.fit(x_train,y_train)

    # Get predictions
    y_prob=clf.predict_proba(np.array(x_test).reshape(-1,1))[:,1]
    y_pred=(y_prob>0.4).astype(int)

    # Score predictions
    score=0
    for yp,yt in zip(y_pred,y_test):
        if yp!=yt: # The classifier predicts wrong, but this is still good
            score+=1

    # Update running accuracy
    z+=(score/len(y_test))
    print("Prediction accuracy after "+str(i+1)+" iterations: "+str(z/(i+1)))

