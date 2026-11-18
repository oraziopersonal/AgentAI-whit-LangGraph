from langchain.messages import AnyMessage
from typing_extensions import TypeDict, Annotated
import operator

class MessageState(TypeDict):
  messages: Annotated[list[AnyMessage], operator.add]
  llm_calls: int
