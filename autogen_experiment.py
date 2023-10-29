import autogen
import docker

# Set API endpoint
# function loads a list of configurations from an environment variable or a json file.
config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        # "model": ["gpt-4", "gpt-4-0314", "gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
        "model": ["gpt-3.5-turbo-0613", "gpt-3.5-turbo"],
    },
)

# create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "seed": 42,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
    },  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)
# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER", # "NEVER" ask, "ALWAYS" ask, ask at "TERMINATE"
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # set to True or image name like "python:3" to use docker
    },
)
# the assistant receives a message from the user_proxy, which contains the task description
user_proxy.initiate_chat(
    assistant,
    # message="""Can you create a python file with a function that prints "hello world" three times?""", #success
    # message="""Can you create a python file with a function that creates a short video of a robot walking in ASCII art?""", #fail, dog animation; line by line
    message="""Can you fix the algorithm in the coding/robot_animation.py file so that it prints multiple lines at once?
    Related to this update, can you also make more Robot animation frames as well? 
    Make sure it's a robot, not a dog. 
    Make sure you save the new code in a new file called robot_animation2.py""",
)