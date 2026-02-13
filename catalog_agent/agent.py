from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from google.adk.models.lite_llm import LiteLlm
from checkout_agent.agent import checkout_agent


def save_cart(
    tool_context: ToolContext,
    category: str,
    item: str,
    quantity: str,
    price: int
):
    tool_context.state["category"] = category
    tool_context.state["item"] = item
    tool_context.state["quantity"] = quantity
    tool_context.state["price"] = price
    tool_context.state["cart_saved"] = True


local_model = LiteLlm(
    model="ollama_chat/qwen2.5:7b-instruct"
)


catalog_agent = LlmAgent(
    name="catalog_agent",
    description="Catalog browsing agent",
    model=local_model,
    instruction="""
SYSTEM ROLE:
You are a CATALOG AGENT.

CATALOG:
Smartphones:
- Pixel 9 – ₹70,000
- iPhone 16 – ₹90,000
- Galaxy S25 – ₹75,000

Laptops:
- MacBook Air M3 – ₹1,10,000
- Dell Inspiron – ₹65,000

Headphones:
- Sony WH-1000XM6 – ₹30,000
- Boat Rockerz – ₹2,000

STATE RULE:
If cart_saved is TRUE, do NOT call save_cart again.

WORKFLOW:
1. Ask which category to browse.
2. Show products.
3. Ask if user wants to add item.
4. Ask quantity.
5. Call save_cart EXACTLY ONCE.
6. Ask:
   "Would you like to proceed to checkout?"

TRANSFER RULE:
- ONLY transfer to checkout_agent AFTER user clearly says YES.

TOOLS:
- save_cart
- transfer_to_agent

FORBIDDEN:
- No silent transfer
- No looping
""",
    tools=[save_cart],
    sub_agents=[checkout_agent]
)
