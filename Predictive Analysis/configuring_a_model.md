# Configuring a model

### Introduction

In the previous chapter we've picked 2 possible Regression models, Random Forest and XGBoost. I will discuss the configurations for both models here. Both models have almost the same configurations, I will therefor explain the configurations once. 


<details> <summary>Random State</summary>
Picking a `random state` is essential for the configurations of your models. Without a `random_state`, the model will always apply a random, new variation of decision trees. To get accurate predictions and results it is important to always have the same decision trees. 

We decided to use `random_state=0` for all our MET prediction models. This way all models would have consistency in the configurations and results could not get manipulated by trying out different random state values. The decision for `random_state=0` is found <a href="https://scikit-learn.org/stable/glossary.html#term-random-state" target="_blank">here</a> [here](https://scikit-learn.org/stable/glossary.html#term-random-state). 

</details>

<details> <summary>Feature Selection</summary>

Text here

Text here

</details>

<details> <summary>Picking the best number of trees</summary>

Text here

Text here

</details>

<details> <summary>Hyperparameter Tuning</summary>

Text here

Text here

</details>

[<  Selecting a model](selecting_a_model.md) — [Training a model >](training_a_model.md) 