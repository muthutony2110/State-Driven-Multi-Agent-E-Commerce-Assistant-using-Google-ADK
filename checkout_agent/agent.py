from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from google.adk.models.lite_llm import LiteLlm
from order_summary_agent.agent import order_summary_agent


def save_shipping_address(
    tool_context: ToolContext,
    address: str
):
    tool_context.state["shipping_address"] = address
    tool_context.state["shipping_address_saved"] = True


local_model = LiteLlm(
    model="ollama_chat/qwen2.5:7b-instruct"
)


checkout_agent = LlmAgent(
    name="checkout_agent",
    description="Checkout agent",
    model=local_model,
    instruction="""
SYSTEM ROLE:
You are a CHECKOUT AGENT.

STATE RULE:
If shipping_address_saved is TRUE:
- Do NOT ask for address again
- Do NOT call save_shipping_address again

WORKFLOW:
1. If shipping_address_saved is FALSE:
   - Ask user for shipping address
2. When provided:
   - Call save_shipping_address EXACTLY ONCE
3. After saving:
   - Ask:
     "Would you like to view your order summary?"
4. If YES:
   - transfer_to_agent(order_summary_agent)

TOOLS:
- save_shipping_address
- transfer_to_agent

FORBIDDEN:
- No silent transfers
- No loops
""",
    tools=[save_shipping_address],
    sub_agents=[order_summary_agent]
)
