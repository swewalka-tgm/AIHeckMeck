import os
import openai
from src.constants import OPENAI_API_KEY

openai.organization = "Personal"
openai.api_key = os.getenv(OPENAI_API_KEY)
openai.Model.list()