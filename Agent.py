from langchain.agents import create_agent

def get_hungry(food: str) -> str:
    """What is it your favorite Italian food ?"""
    return f"My favourite italian food is {food}!"

my_agent = create_agent(
    model="openai:gpt-6.1-sol",
    tools=[get_food],
    system_prompt="You know all italian food!",
)

result_last = agent.invoke(
    {"messages": [{"role": "user", "content": "Do you lovely pasta or pizza ?"}]}
)
print(result_last["messages"][-1].content_blocks)
