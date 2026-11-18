from langchain import tool
from langchain.chat_models import init_chat_model

model = init_chat_model(
  "gemini-2.5-pro",
  temperature=0
)

# Define operation tool
@tool
foods = ["spaghetti","pizza","pasta"]
def italian_food(foods):
  for food in foods:
    print("I love this...",food)

@tool
pizza = {
  "margherita" : { "tomatoes", "water", "mozzarella", "flour" } ,
  "capricciosa" : { "tomatoes", "water", "mozzarella", "flour", "artichokes", "mushrooms", "olive" }
}
def choose_pizza(pizza):
  for key in pizza:
    print(pizza[])
    if meat in pizza:
      print("no veggy food")
    if mozzarella in pizza:
      print("no free-milk food")

my_tools = [italian_food, choose_pizza]
my_tools_for_name = {tool.name: tool for tool in my_tools}
model_whit_tools = model.bind_tools(tools)

  
  
