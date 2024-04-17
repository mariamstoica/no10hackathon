# Functions to create question from a news headline using ChatGPT
import requests

def openai_chat_completion(sys_prompt, user_prompt, openai_key):
  """Get ChatGPT text response to query"""

  url = "https://api.openai.com/v1/chat/completions"
        
  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {openai_key}"
  }
      
  data = {
      "model": "gpt-3.5-turbo",
      "messages": [
          {
              "role": "system",
              "content": sys_prompt
          },
          {
              "role": "user",
              "content": user_prompt
          }
      ]
  }

  response = requests.post(url, headers=headers, json=data)
  return response.json()['choices'][0]['message']['content']


def create_question_from_headline(headline, questioner_type, openai_key):
  """
  Generate a question from a news headline a person (questioner_type) may ask the PM
  using ChatGPT chart completion.
  headline : str. The newsheadline
  questioner_type : str. Type of person asking question (e.g. member of public, expert journalist).
  openai_key : str. Open API key.
  """

  question = openai_chat_completion(
      sys_prompt = f"You are a {questioner_type} and have just read the news headline given below. \
      Based on this news headline, please can you come up with a difficult question to ask the \
      Prime Minister of the UK which addresses issues that are in the public interest.",
                       user_prompt = headline,
                       openai_key = openai_key)
  
  return question

