import autogen #importing autogen

#initialise openhermes model from terminal using litellm --model openhermes, got port base
topic = "algebra" 

config_list = [
    {
         'api_base': 'http://0.0.0.0:8000',
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
        "work_dir": "coding",
        "use_docker":False

    }
)

#agents interfacing

#prompts the research agent to make research according to the researcher's role predefined above
user_proxy.initiate_chat(researcher,
                          message=researcher_task
                          )
response1 = researcher.get_response()

#generating response from the researcher and sends it to the writer agent
generated_response_r = researcher.a_send(response1, recipient=writer) 
writer.a_receive(generated_response_r, sender=researcher) #writer recieves this response

#generating writer's response and sends it to the examiner agent
response2 = writer.get_response()
generated_response_w = writer.a_send(response2, recipient=examiner) 
examiner.a_receive(generated_response_w, sender=writer)

#prompts examiner agent with examiner's task
user_proxy.initiate_chat(examiner,
                          message=examiner_role
                          )



