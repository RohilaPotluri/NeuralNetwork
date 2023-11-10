Name: Rohila Potluri
UCM Id: 700744509
Video link: https://drive.google.com/file/d/1GIqqH0IMuxYW7Ybh0dDOIG8wSvxyX4I1/view?usp=sharing

Loaded all the necessary libraries and created a model function that returns a keras model with the specified hypereters. The hhypermeters here are tuned to be number of LSTM units, drop ot rate and learning rate.
Saved the model and used the saved model to predict on new text data. Applied GridSearchCV on the source code provided in the class. The keras classifier is used as a wrapper for create_model funcytion which is used as an estimator for gridsearchCV. 
