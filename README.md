# Bigram_Mlmodel
Implemented a Bigram Language Model to predict the next word in a sequence based on the preceding word. The model is built using a statistical approach that leverages bigram probabilities, and it includes techniques for evaluating and improving the model's performance through smoothing. 

Features:

Bigram Probability Calculation: Computes the probability of a word given the previous word using bigram frequencies.
Log Likelihood and Loss Function: Calculates the log likelihood of a sequence and the corresponding loss function to evaluate model performance.
Smoothing Techniques: Implements additive (Laplace) smoothing to handle unseen bigrams and reduce the impact of zero probabilities.
Model Evaluation: Evaluates the model using perplexity and cross-entropy metrics to assess its quality and predictive power.

Dataset: The dataset used is names.txt a large dataset that consits of approx 32K words
