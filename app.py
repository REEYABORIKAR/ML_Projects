import gradio as gr
import pickle
import pandas as pd

# Load model and preprocessor
with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("artifacts/preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)


def predict(
    gender,
    race_ethnicity,
    parental_level_of_education,
    lunch,
    test_preparation_course,
    reading_score,
    writing_score,
):
    input_data = pd.DataFrame(
        [[
            gender,
            race_ethnicity,
            parental_level_of_education,
            lunch,
            test_preparation_course,
            reading_score,
            writing_score,
        ]],
        columns=[
            "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course",
            "reading_score",
            "writing_score",
        ],
    )

    transformed_data = preprocessor.transform(input_data)
    prediction = model.predict(transformed_data)

    return float(prediction[0])


interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(["male", "female"], label="Gender"),
        gr.Dropdown(
            ["group A", "group B", "group C", "group D", "group E"],
            label="Race/Ethnicity",
        ),
        gr.Dropdown(
            [
                "associate's degree",
                "bachelor's degree",
                "high school",
                "master's degree",
                "some college",
                "some high school",
            ],
            label="Parental Level of Education",
        ),
        gr.Dropdown(["free/reduced", "standard"], label="Lunch"),
        gr.Dropdown(["none", "completed"], label="Test Preparation Course"),
        gr.Number(label="Reading Score"),
        gr.Number(label="Writing Score"),
    ],
    outputs=gr.Number(label="Predicted Math Score"),
    title="Student Performance Predictor",
    description="End-to-End Machine Learning model deployed on Hugging Face Spaces",
)

interface.launch()
