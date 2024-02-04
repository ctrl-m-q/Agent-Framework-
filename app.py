import autogen #importing autogen
from ollama import openhermes #import ollama library

#initialise openhermes model
openhermes_model = openhermes


config_list = [
    {
         'api_key': ''

    }
]
llm_config={
        "config_list": config_list
        
    }


#creating agents

researcher = autogen.AssistantAgent(
    name="researcher",
    llm_config=llm_config
    )


writer = autogen.AssistantAgent(
   name= "writer", llm_config=llm_config
   )

examiner = autogen.AssistantAgent(
    name="examiner", llm_config=llm_config
    )

#assign roles to agents

researcher_task = "give ideas for teaching a newbie {}.".format(topic)
writer_role = "Use the Researcher’s ideas to write a piece of text to explain the {}.".format(topic)
examiner_role = "Craft 3 test questions to evaluate the newbie's understanding of the created text, along with the correct answers.".format(topic)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    code_execution_config = {
        "work_dir": "coding"
    }
)

#agents interfacing

user_proxy.initiate_chat(researcher, message=researcher_task,  clear_history=False)
response1 = researcher.get_response()
generated_response_r = researcher.a_send(response1, recipient=writer) #generate response from user query
writer.a_receive(generated_response_r, sender=researcher) #get the generated response from researcher and act on it
#user_proxy.initiate_chat(writer, message=writer_role, clear_history=False)#prompt the writer agent with task
response2 = writer.get_response()
generated_response_w = writer.a_send(response2, recipient=examiner) #generate response from user query
examiner.a_receive(generated_response_w, sender=writer)
user_proxy.initiate_chat(examiner, message=examiner_role, clear_history=False)



