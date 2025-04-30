import pandas as pd
from src.preprocessing import clean_text
from src.model import build_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

def run_training():
    # Load and clean data
    df = pd.read_csv('data/raw/Road Accident Data.csv')
    df['Accident_Severity'] = df['Accident_Severity'].replace('Fetal', 'Fatal')

    # Generate synthetic description
    df['description'] = (
        df['Day_of_Week'].astype(str) + ' ' +
        df['Junction_Control'].astype(str) + ' ' +
        df['Junction_Detail'].astype(str) + ' ' +
        df['Light_Conditions'].astype(str) + ' ' +
        df['Road_Type'].astype(str) + ' ' +
        df['Weather_Conditions'].astype(str)
    )

    # Clean text data
    df['cleaned'] = df['description'].apply(clean_text)

    # Save cleaned data
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/cleaned_accident_data.csv', index=False)

    # Feature/Label split
    X = df['cleaned']
    y = df['Accident_Severity']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = build_model()
    model.fit(X_train, y_train)

    # Save model
    os.makedirs('saved_models', exist_ok=True)
    joblib.dump(model, 'saved_models/nlp_model.pkl')

    # Save predictions
    y_pred = model.predict(X_test)
    os.makedirs('data/processed', exist_ok=True)
    pd.DataFrame({
        'Text': X_test,
        'Actual': y_test,
        'Predicted': y_pred
    }).to_csv('data/processed/model_predictions.csv', index=False)

    # Print evaluation
    print("\n--- Evaluation Report ---\n")
    print(classification_report(y_test, y_pred))

    return model, X_test, y_test
