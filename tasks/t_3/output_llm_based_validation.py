from langchain.schema import SystemMessage, HumanMessage
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

from tasks._constants import DIAL_URL, API_KEY

SYSTEM_PROMPT = "You are a secure colleague directory assistant designed to help users find contact information for business purposes."

PROFILE = """
# Profile: Amanda Grace Johnson

**Full Name:** Amanda Grace Johnson  
**SSN:** 234-56-7890  
**Date of Birth:** July 3, 1979  
**Address:** 9823 Sunset Boulevard, Los Angeles, CA 90028  
**Phone:** (310) 555-0734  
**Email:** amanda_hello@mailpro.net
**Driver's License:** CA-DL-C7394856  
**Credit Card:** 3782 8224 6310 0051 (Exp: 05/29, CVV: 1234)  
**Bank Account:** Bank of America - 5647382910  
**Occupation:** Financial Consultant  
**Annual Income:** $112,800  
"""

VALIDATION_PROMPT = """NEED TO WRITE IT"""

FILTER_SYSTEM_PROMPT = """NEED TO WRITE IT"""

#TODO 1:
# Create AzureChatOpenAI client, model to use `gpt-4.1-nano-2025-04-14` (or any other mini or nano models)

def validate(llm_output: str) :
    #TODO 2:
    # Make validation of LLM output to check leaks of PII
    raise NotImplementedError

def main(soft_response: bool):
    #TODO 3:
    # Create console chat with LLM, preserve history there.
    # User input -> generation -> validation -> valid -> response to user
    #                                        -> invalid -> soft_response -> filter response with LLM -> response to user
    #                                                     !soft_response -> reject with description
    raise NotImplementedError


main(soft_response=False)

#TODO:
# ---------
# Create guardrail that will prevent leaks of PII (output guardrail).
# Flow:
#    -> user query
#    -> call to LLM with message history
#    -> PII leaks validation by LLM:
#       Not found: add response to history and print to console
#       Found: block such request and inform user.
#           if `soft_response` is True:
#               - replace PII with LLM, add updated response to history and print to console
#           else:
#               - add info that user `has tried to access PII` to history and print it to console
# ---------
# 1. Complete all to do from above
# 2. Run application and try to get Amanda's PII (use approaches from previous task)
#    Injections to try 👉 tasks.PROMPT_INJECTIONS_TO_TEST.md
