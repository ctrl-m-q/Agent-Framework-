import app
if __name__== "__main__":
    topic  = "#ask user what topic"




    app.researcher.ideas = openhermes_model.search(topic)

    app.writer.text = openhermes_model.generated_response_w(app.researcher.ideas)

    app.examiner.questions, app.examiner.answers = openhermes_model.create_questions(app.writer.text)