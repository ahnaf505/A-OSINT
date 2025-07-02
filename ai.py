from fireworks import LLM

class LLMChatSession:
    def __init__(self, model: str, api_key: str, deployment_type: str = "auto"):
        self.llm = LLM(model=model, deployment_type=deployment_type, api_key=api_key)
        self.messages = []  # store conversation context

    def send(self, prompt: str) -> str:
        self.messages.append({"role": "user", "content": prompt})
        response = self.llm.chat.completions.create(messages=self.messages)
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def reset(self):
        self.messages.clear()

    def history(self):
        return self.messages
