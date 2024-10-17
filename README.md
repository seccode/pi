# Pi
The digits of pi are probably not random; we can demonstrate this by predicting the digits with a Random Forest Classifier

# Methodology
The feature vector (x) is the index of the digit of pi. The target vector (y) is index in [0,1,2,3,4].

# Results
The model predicts wrong, to a statistically significant degree. By using label inversion, the model predicts right. The expected probability of seeing a 0 vs. 1 is 0.50015. The classifier's accuracy is 0.5015. The z-score (statistical significance) is 3.82 standard deviations which is statistically significant.

<img src="pi.webp" alt="firn" width="400">
Pi
