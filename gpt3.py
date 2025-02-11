from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-ev1dJ": {
    "files": "",
    "background_color": "",
    "chat_icon": "",
    "input_value": "你好",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "ParseData-CNMlq": {
    "sep": "\n",
    "template": "{text}"
  },
  "SplitText-UG94Z": {
    "chunk_overlap": 200,
    "chunk_size": 1000,
    "separator": "\n"
  },
  "ChatOutput-TMXAD": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "AstraDB-XPpzv": {
    "advanced_search_filter": "{}",
    "api_endpoint": "https://a5554046-c718-4b6d-bd60-8dece288763a-us-east1.apps.astra.datastax.com",
    "astradb_vectorstore_kwargs": "{}",
    "autodetect_collection": True,
    "collection_name": "gabeiedu_nvdia",
    "content_field": "",
    "d_api_endpoint": "",
    "deletion_field": "",
    "embedding_choice": "Astra Vectorize",
    "environment": "",
    "ignore_invalid_documents": False,
    "keyspace": "",
    "number_of_results": 4,
    "search_query": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "token": "ASTRA_DB_APPLICATION_TOKEN"
  },
  "File-IJCjj": {
    "path": "testrag.pdf",
    "concurrency_multithreading": 4,
    "delete_server_file_after_processing": True,
    "ignore_unspecified_files": False,
    "ignore_unsupported_extensions": True,
    "silent_errors": False,
    "use_multithreading": False
  },
  "Agent-Z5wur": {
    "add_current_date_tool": True,
    "agent_description": "A helpful assistant with access to the following tools:",
    "agent_llm": "OpenAI",
    "api_key": "Openai_key",
    "handle_parsing_errors": True,
    "input_value": "",
    "json_mode": False,
    "max_iterations": 15,
    "max_tokens": None,
    "model_kwargs": {},
    "model_name": "gpt-4o-mini",
    "n_messages": 100,
    "openai_api_base": "",
    "order": "Ascending",
    "seed": 1,
    "sender": "Machine and User",
    "sender_name": "",
    "session_id": "",
    "system_prompt": "You are a helpful assistant that can use tools to answer questions and perform tasks.",
    "temperature": 0.1,
    "template": "{sender_name}: {text}",
    "verbose": True
  },
  "Prompt-9yHS5": {
    "template": "判断优先级1：如果此次回复是你第一次回复，请你在回答用户问题前，必须先在你的回复中粘贴{first}内容作为第一次回答的开头，在{first}里每到符号；就必须另起一行，如果不是第一次回复，则不用带{first}中的内容。\n\n判断优先级2：在以上基础上，你的主要目的是利用联网信息准确回答用户问题，如果你不知道答案，就说你不清楚具体答案，考虑问题时参考{back}里面的背景信息。\n\n判断优先级3：如果用户的问题和公司的数据库数据高度相似，那么请使用Retrieval-augmented generation（RAG）来获取并呈现最相关的信息：{Results}\n",
    "tool_placeholder": "",
    "first": "Cheers!\n(“￣▽￣)-o█ █o-(￣▽￣”)/\n这里是您的专属留学咨询AI小助手：小噶 ヽ(・×・´)ゞ\n有关留学的任何问题都可以先跟我聊聊哟！\n另外，为了让我更聪明 ٩(๑•̀ω•́๑)۶\n更好地提供针对您个人的服务，您不妨先提供我以下信息：\n您本科、硕士的学校，GPA，毕业信息；\n参考格式：【本科：原神大学，2020-2024，4.00；硕士：海拉鲁大学，2024-2025，无GPA；2025毕业。】\n您想要读博的地区；\n参考格式：【读博想去欧洲、美国。】\n您想要读的专业；\n参考格式：【读博想学AI或金融。】\n您是否接受自费，自费的话预算有多少；如果您需要奖学金，请表达意愿强度；\n参考格式：【接受自费，每年30万RMB；非常需要奖学金！！！！】\n您入学PhD前是否需要GAP year；\n参考格式【需要gap 1 year。】",
    "Results": "",
    "back": ""
  }
}

result = run_flow_from_json(flow="Vector Store RAG.json",
                            session_id="1", # provide a session id if you want to use session state
                            fallback_to_env_vars=False, # False by default
                            tweaks=TWEAKS)