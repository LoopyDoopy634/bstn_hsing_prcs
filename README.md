
# Boston Housing Prices

This project is an end-to-end machine learning case study focused on predicting the median value of homes in Boston using the classic Boston Housing dataset. The goal was to explore the data, build and compare different regression models, and use the best-performing model to make predictions on new, unseen data.

Through a **"vibe coding"** approach that prioritized intuition and rapid iteration, the project involved:

* **Data Cleaning**: Preprocessing a raw dataset to add headers and ensure it was ready for analysis.

* **Exploratory Data Analysis (EDA)**: Creating visualizations like histograms, scatter plots, and heatmaps to understand the relationships between features like the number of rooms (RM) and neighborhood status (LSTAT) with the house price (MEDV).

* **Model Building & Comparison**: Training and evaluating several models, including:

    * A single-feature Linear Regression model.

    * A single-feature Decision Tree Regressor, which performed better.

    * A multi-feature Decision Tree Regressor using RM and LSTAT, which achieved an **R-squared of 0.76**.

* **Model Interpretation & Application**: Visualizing the final Decision Tree to understand its internal logic and using the trained model to predict prices for hypothetical houses.

The dataset was taken from Kaggle: [The Boston Hosuing Dataset](https://www.kaggle.com/code/prasadperera/the-boston-housing-dataset "Go to Kaggle's website")



 





## Installation

The following Python libraries have to be installed before running the scripts in this project:

  * pandas
  * scikit-learn
  * matplotlib
  * joblib
  * seaborn

You can install these packages using pip: 

```bash
  pip install pandas scikit-learn matplotlib joblib seaborn
```
    
## Run Locally

**1. Clone the project**

```bash
  git clone https://github.com/LoopyDoopy634/bstn_hsing_prcs
```

**2. Go to the project directory**

```bash
  cd bstn_hsing_prcs
```
**3. Install the required Python packages (Check "Installation" above).**

**4. Run the scripts in order to execute the full data science pipeline from your terminal.**

  * First prepare the dataset (You only need to do this once):

  ```bash
    python add_headers.py
```
  * Next, train the model:

```bash
  python train_multi_feature_model.py
```

  * Then, visualize the trained model:

```bash
  python visualize_multi_feature_tree.py
```  
  * Finally, use the model to make new predictions:

  ```bash
    python predict_price.py
```  

*Note: The other scripts can be run similarly. First run the model script followed by the visualization script.*


## Features

 * **End-to-End Workflow:** A complete machine learning pipeline from raw data cleaning and exploratory analysis to model training, evaluation, and final prediction.

 * **Model Comparison:** Implements and evaluates both a Linear Regression and a Decision Tree model to find the best-performing algorithm for the task.

 * **Interpretable Machine Learning:** Includes scripts to visualize the Decision Tree, providing a clear and intuitive look into the model's decision-making logic.

 * **Modular and Reusable Code:** The project is structured with separate, single-purpose scripts for data preparation, training, visualization, and prediction, promoting clarity and reusability.

 * **Iterative Model Improvement:** Demonstrates how model accuracy is significantly improved (R² from 0.51 to 0.76) by incorporating more relevant features identified during the analysis phase.


## Screenshots

![Histogram](https://drive.google.com/uc?export=view&id=1WK_62YRh-9QFheVGSp5E1pNx4jd3bqWu)


![Scatter Plot](https://drive.google.com/uc?export=view&id=1TaOMhMutB2AQ0Wwglw1GZi8eN9OlXeip)

![Heatmap](https://drive.google.com/uc?export=view&id=1tv3SUIGPMZakDcbILndX3joNvCMcE6Cb)

![Single Feature Decision Tree](https://drive.google.com/uc?export=view&id=1iB7eQdRIxh2jnWQ7gZ7iFNboBy980tr_)

![Multi Feature Decision Tree](https://drive.google.com/uc?export=view&id=12llKUqkOUbZNxsQycJVKaFrLETH4PbWI)

![Housing Price Prediction](https://drive.google.com/uc?export=view&id=1PA5IjHVbdXGXqAC8VL1EKpuG54FNoodY)


