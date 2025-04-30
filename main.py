from src.train import run_training
from src.evaluate import evaluate, save_confusion_matrix_png

if __name__ == "__main__":
    # Train model and get test data
    model, X_test, y_test = run_training()

    # Evaluate model and print classification report
    evaluate(model, X_test, y_test)

    # Predict and save confusion matrix
    y_pred = model.predict(X_test)
    save_confusion_matrix_png(y_test, y_pred, labels=model.classes_)
