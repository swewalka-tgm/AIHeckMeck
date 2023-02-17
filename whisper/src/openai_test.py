import os
import openai
openai.organization = "Personal"
openai.api_key = os.getenv("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")
openai.Model.list()