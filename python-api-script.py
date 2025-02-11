from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-kKhri": {},
  "Prompt-KDSi5": {},
  "ChatOutput-Vr3Q7": {},
  "OpenAIModel-4xYtx": {}
}

result = run_flow_from_json(flow="./basic-prompting-local.json",
                            input_value="tell me about something interesting",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)

print(result)
