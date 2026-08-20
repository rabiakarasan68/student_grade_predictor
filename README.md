# Student Grade Predictor

A machine learning project that predicts a student's final grade based on their **midterm exam score** and **participation score**.

The project compares two different regression algorithms, selects the model with the lower prediction error, and provides both a command-line interface and a graphical user interface for making predictions.

## Features

* Predicts final grades using:

  * Midterm (`vize`) score
  * Participation (`katilim`) score
* Compares two machine learning models:

  * Linear Regression
  * Random Forest Regressor
* Evaluates models using Mean Absolute Error (MAE)
* Automatically selects the model with the lowest MAE
* Saves the best model using Joblib
* Converts predicted numerical grades into letter grades
* Provides command-line prediction
* Provides a Tkinter-based graphical user interface
* Displays a prediction graph in the GUI

## Machine Learning Workflow

The project follows these steps:

1. Load the dataset from `data.csv`
2. Select `vize` and `katilim` as input features
3. Use `final` as the target variable
4. Split the dataset into training and test sets
5. Train a Linear Regression model
6. Train a Random Forest Regressor model
7. Calculate the Mean Absolute Error (MAE) for both models
8. Select the model with the lower error
9. Save the best model as `model.pkl`
10. Use the trained model to predict final grades

## Dataset

The dataset is stored in `data.csv`.

It contains three columns:

| Column    | Description         |
| --------- | ------------------- |
| `vize`    | Midterm exam score  |
| `katilim` | Participation score |
| `final`   | Final exam score    |

Example:

```csv
vize,katilim,final
78,11,47.64
18,66,29.17
63,16,39.78
6,83,26.74
29,47,38.20
```

The dataset contains synthetic student grade data created for educational and machine learning purposes.

## Models

### Linear Regression

Linear Regression is used to model the relationship between the input features and the final grade.

```python
lr = LinearRegression()
lr.fit(X_train, y_train)
```

### Random Forest Regressor

Random Forest Regressor is also trained using the same training data.

```python
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
```

### Model Selection

Both models are evaluated using Mean Absolute Error:

```python
lr_error = mean_absolute_error(y_test, lr_pred)
rf_error = mean_absolute_error(y_test, rf_pred)
```

The model with the lower MAE is selected as the best model.

```python
if lr_error < rf_error:
    best_model = lr
else:
    best_model = rf
```

The selected model is then saved as:

```text
model.pkl
```

## Letter Grade System

The predicted final score is converted into a letter grade using the following scale:

|  Score | Letter Grade |
| -----: | :----------- |
| 90–100 | AA           |
|  80–89 | BA           |
|  70–79 | BB           |
|  60–69 | CB           |
|  50–59 | CC           |
|   0–49 | FF           |

## Project Structure

```text
student-grade-predictor/
│
├── data.csv          # Dataset
├── train.py          # Model training and comparison
├── predict.py        # Command-line prediction
├── utils.py          # Letter grade conversion
├── gui.py            # Tkinter graphical interface
├── model.pkl         # Trained best model
├── requirements.txt  # Required Python libraries
├── README.md         # Project documentation
└── .gitignore        # Git ignored files
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/student-grade-predictor.git
```

Navigate to the project directory:

```bash
cd student-grade-predictor
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Train the Model

Run:

```bash
python train.py
```

This will:

* Load `data.csv`
* Split the dataset into training and test sets
* Train Linear Regression
* Train Random Forest
* Calculate MAE values
* Select the best model
* Save the model as `model.pkl`
* Display a prediction performance graph

### 2. Make a Prediction from the Terminal

Run:

```bash
python predict.py
```

The program asks for:

```text
Vize notu:
Katılım:
```

Then it displays the predicted final grade and corresponding letter grade.

Example:

```text
-----Sonuç-----
Tahmin edilen final notu: 72.45
Harf Notu: BB
```

### 3. Use the Graphical Interface

Run:

```bash
python gui.py
```

The Tkinter interface allows the user to:

* Enter a midterm score
* Enter a participation score
* Predict the final grade
* Display the corresponding letter grade
* Display a prediction graph

## Technologies

* Python
* Pandas
* Scikit-learn
* Joblib
* Matplotlib
* Tkinter

## Evaluation Metric

The models are evaluated using **Mean Absolute Error (MAE)**.

MAE measures the average absolute difference between the actual final grades and the predicted final grades.

A lower MAE indicates better prediction performance.

## Purpose

This project was developed as a practical machine learning project to demonstrate:

* Regression algorithms
* Train/test data splitting
* Model evaluation
* Model comparison
* Model persistence
* Prediction
* Basic graphical user interface development

## Future Improvements

Possible future improvements include:

* Adding more student features such as homework, project, and exam scores
* Improving the dataset with real-world anonymized data
* Testing additional regression algorithms
* Adding input validation to the GUI
* Improving the visualization of prediction results
* Adding a web-based interface using Streamlit or Flask

## License

This project is intended for educational purposes.
