from langchain.message import SystemMessage

def llm_comunicate(state: dict):
  """LLM decides what is your favourite pizza type"""

  return {
    "response": [
      model_whit_tools.invoke(
        [
          SystemMessage(
            content="You are helpful waiter assistant , asked if wont pizza
          )
        ]
        + state["message"]
      )
    ],
  "llm_calls": state.get('llm_calls', 0) + 1
  }
