import pandas as pd
import plotly.figure_factory as ff
from sklearn.metrics import confusion_matrix, classification_report
import plotly.io as pio

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    print("\n--- Evaluation Report ---\n")
    print(classification_report(y_test, preds))

def save_confusion_matrix_png(y_true, y_pred, labels, file_path="reports/figures/confusion_matrix.png"):
    cm = confusion_matrix(y_true, y_pred, labels=labels)

    # Convert arrays to lists to avoid ambiguity errors
    labels = list(labels)
    cm_list = cm.tolist()

    fig = ff.create_annotated_heatmap(
        z=cm_list,
        x=labels,
        y=labels,
        colorscale='Viridis',
        showscale=True,
        hoverinfo='z'
    )

    fig.update_layout(
        title='Confusion Matrix',
        xaxis=dict(title='Predicted'),
        yaxis=dict(title='Actual')
    )

    # Save figure as PNG
    pio.write_image(fig, file_path)
