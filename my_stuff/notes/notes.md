# Autogen Notes

## "Multi-agent Conversation Framework" Notes

https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat

Agents:
- UserProxyAgent
    - You can configure when the human is prompted: ALWAYS, NEVER, TERMINATE (see options)
    - If there is no human input, this triggers code execution automatically (by default. See code
    execution config). LLM based response is disabled by default, so if there is no code, it won't
    say anything. (You can enable it. If I am running with user input enabled, i would want to know
    there is no code and then I would say something rather than just returning nothing.)
- AssistantAgent - Normal AI assistant