import pickle
from pathlib import Path
from os import listdir
from os.path import isfile, join
import pandas as pd

from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI



myPath = f'{Path.home()}/airo/data'
onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath,f))]
for f in onlyfiles:
    #should we concat them one by one
    #will this consume more memory
    if  first:
        with open (join(myPath,f),'rb') as file:
            data1 = pickle.load(file)
            first = False
    else:
        with open (join(myPath,f),'rb') as file:
            data1 = pd.concat([data1,pickle.load(file)])

#agent alternative 1            
agent = create_pandas_dataframe_agent(OpenAI(temperature=0), data1, verbose=True)

#agent alternative 2
agent = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    data1,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)
agent.run("how many rows are there?")