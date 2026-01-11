import gradio as gr
from src.pipeline.predict_pipepline import CustomData, PredictPipeline

pipeline = PredictPipeline()

def predict(gender, race_ethnicity, parental_level_of_education,
            lunch, test_preparation_course, reading_score, writing_score):

    data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    df = data.get_data_as_data_frame()
    result = pipeline.predict(df)
    return result[0]

interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(["male", "female"], label="Gender"),
        gr.Dropdown(["group A", "group B", "group C", "group D", "group E"], label="Race"),
        gr.Dropdown(["associate's degree","bachelor's degree","high school","master's degree","some college","some high school"], label="Parental Education"),
        gr.Dropdown(["free/reduced", "standard"], label="Lunch"),
        gr.Dropdown(["none", "completed"], label="Test Prep"),
        gr.Number(label="Reading Score"),
        gr.Number(label="Writing Score"),
    ],
    outputs="number",
    title="Student Performance Predictor"
)

interface.launch()
