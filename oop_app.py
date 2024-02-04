import autogen

class AgentWorkflow:


    def __init__(self, topic):
        self.topic = topic
        self.researcher = autogen.AssistantAgent(
            "researcher",
            llm_config={
                'model': 'openhermes',
                'base': 'http://0.0.0.0:8000',
                'api_key': ''
            }

        )

        self.writer = autogen.AssistantAgent(
            "writer",
            llm_config={
                'model': 'openhermes',
                'base': 'http://0.0.0.0:8000',
                'api_key': ''
            }

        )

        self.examiner = autogen.AssistantAgent(
            "examiner",
            llm_config={
                'model': 'openhermes',
                'base': 'http://0.0.0.0:8000',
                'api_key': ''
            }
        )

        self.UserProxyAgent = autogen.UserProxyAgent(
             "user_proxy",
             code_execution_config = {
                 "work_dir": "coding",
                 "use_docker":False
             }
        )


        

        def initiate_chat(self):
            researcher_task = f"give ideas for teaching someone new to the subject {self.topic}"
            writer_role = f"Use the Researcher’s ideas to write a piece of text to explain the {self.topic}."
            examiner_role = f"Craft 3 test questions to evaluate the person's understanding of the {self.topic}, along with the correct answers."

            self.UserProxyAgent.initiate_chat(messages=[researcher_task], recipient=self.researcher)
            

