import autogen #importing autogen

#initialise openhermes model
openhermes_model = autogen.load_model("openhermes")

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
    llm_config=llm_config)


writer = autogen.AssistantAgent(
   name= "writer", llm_config=llm_config)

examiner = autogen.AssistantAgent(
    name="examiner", llm_config=llm_config)

#assign roles to agents
researcher_task = "Develop ideas for teaching someone new to the f'{{topic}}"
writer_role = "Use the Researcher’s ideas to write a piece of text to explain the f'{{topic}}"
examiner_role = "Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers. In other words: test whether a student has fully understood the text."

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
user_proxy.initiate_chat(writer, message=writer_role, clear_history=False)#prompt the writer agent with task
response2 = writer.get_response()
generated_response_w = writer.a_send(response2, recipient=examiner) #generate response from user query
examiner.a_receive(generated_response_w, sender=writer)
user_proxy.initiate_chat(examiner, message=examiner_role, clear_history=False)





#how do i generate response from the query given and parse this response into the other agents?
#should i just use these simple prompts or use what's above?

task2 = "Use the Researcher’s ideas to write a piece of text to explain the topic"
user_proxy.initiate_chat(writer, message=task2, clear_history=False)

