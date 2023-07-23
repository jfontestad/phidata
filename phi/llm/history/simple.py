from typing import Optional, List

from phi.llm.history.base import LLMHistory
from phi.llm.schemas import Message


class SimpleConversationHistory(LLMHistory):
    max_messages: int = 6
    max_tokens: Optional[int] = None
    include_assistant_responses: bool = True

    def get_formatted_history(self) -> str:
        """Returns a formatted chat history for the LLM prompt"""

        history = ""
        messages_in_history: List[Message] = []
        for message in self.messages[::-1]:
            if message.role == "user":
                messages_in_history.insert(0, message)
            if message.role == "assistant" and self.include_assistant_responses:
                messages_in_history.insert(0, message)
            if len(messages_in_history) >= self.max_history_messages:
                break

        for message in messages_in_history:
            if message.role == "user":
                history += "\n---\n"
            history += f"{message.role.upper()}: {message.content}\n"
        return history