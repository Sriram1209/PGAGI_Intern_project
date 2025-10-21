# This file marks the bot_logic directory as a Python package.
# You can include module initializations or imports here if needed.

from .prompt_manager import get_greeting_prompt, get_tech_questions_prompt
from .llm_handler import generate_response
from .context_manager import update_context, check_exit
