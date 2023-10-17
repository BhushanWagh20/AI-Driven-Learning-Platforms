from autogen import AssistantAgent,UserProxyAgent


config_list=[
    {
        "model":"gpt-3.5-turbo",
        "api_key":"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"
    }

]
llm_config = {
    # "request_timeout":600,
    # "seed":42,
    "config_list":config_list,
    "temperature":0
    }

# create a instance of AssistantAgent
assistant = AssistantAgent(
    name='assistant',
    llm_config=llm_config
)
# create a instance of UserProxyAgent
user_proxy = UserProxyAgent(
    name='user_proxy',
    system_message = 'A Human input',
    human_input_mode='ALWAYS',
    # max_consecutive_auto_reply=10,
    # is_termination_msg=lambda x:x.get("contemt","").rstrip().endswith("TERMINATE"),
    # code_execution_config={"work_dir":"web"},
    llm_config=llm_config
)

task = """
1. If an = n2 – 1 and an = 99 then the value of n is
a) 100 b) 10 c) 9 d) 99
2. If an = 2n2 – 1 then the value of 4th term is
a) 32 b) 30 c) 31 d) 18
3. If an = 2n + 1 then the common difference of the AP is
a) 3 b) 5 c) 2 d) 1
4. The general form of an A.P is
a) a, ar, ar2,... . b) a, a + d, a + 2d, ... c) a, a–d, a–2d,.... d),.... a a d a 2d
5. In an A.P the common difference is 3 first term is 1 then the value of 10th
term is
a) 28 b) 27 c) 25 d) 40c



your expert in mathematics i provided some question your task is to ask me the question and given options one by one if my answer is correct or not verify and answer that question then you directly move to another question,lastly you give me feedback for my performance out of 100% also give me suggestion to improvement understood """
user_proxy.initiate_chat(
    assistant,
    message = task
)