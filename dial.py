import os
from google.cloud import dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cl.json"
project_id = 'barrestaurante-eltri-ngul-xpxa'
session_id = 'me'

session_client = dialogflow.SessionsClient()
session_path = session_client.session_path(project_id, session_id)

tx=input()

text_input = dialogflow.TextInput(text=tx, language_code="es-ES")
query_input = dialogflow.QueryInput(text=text_input)

response = session_client.detect_intent(session=session_path, query_input=query_input)

fulfillment_messages = response.query_result.fulfillment_messages

text_response = ""
seen_paragraphs = set()
for message in fulfillment_messages:
    if message.text.text:
        for paragraph in message.text.text:
            if paragraph not in seen_paragraphs:
                text_response += paragraph + "\n"
                seen_paragraphs.add(paragraph)

# Print the text response
print("Text response:\n", text_response)
