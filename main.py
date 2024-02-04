import app

if __name__ == "__main__":
    topic = input("Enter the topic: " )
    
    # Pass the topic to the methods in app.py
    app.researcher_task = "give ideas for teaching a newbie {}.".format(topic)
    app.writer_role = "Use the Researcher’s ideas to write a piece of text to explain the {}.".format(topic)
    app.examiner_role = "Craft 3 test questions to evaluate the newbie's understanding of the created text, along with the correct answers.".format(topic)

#since the openhermes is not going to be imported traditionally but used through litellm, the use of the statements below is not needed so i will be commenting it out
"""
    openhermes_model = app.openhermes_model
    app.researcher.ideas = openhermes_model.search(topic)

    app.writer.text = openhermes_model.generated_response_w(app.researcher.ideas)

    app.examiner.questions, app.examiner.answers = openhermes_model.create_questions(app.writer.text)

""" 
   