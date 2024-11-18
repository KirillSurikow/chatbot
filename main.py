import json
import os
import time
from flask import Flask, request, jsonify
import openai
from openai import OpenAI
import functions


from packaging import version
# from dotenv import load_dotenv

# load_dotenv()


required_version = version.parse("1.1.1")
current_version = version.parse(openai.__version__)

if current_version < required_version:
  raise ValueError(
      f"Error: OpenAI version {openai.__version__} is less than the required version 1.1.1"
  )
else:
  print("OpenAI version is compatible.")

app = Flask(__name__)
client = OpenAI(api_key=OPENAI_API_KEY)


@app.route('/start', methods=['GET'])
def start_conversation():
  thread = client.beta.threads.create()
  print("New conversation started with thread ID:", thread.id)
  return jsonify({"thread_id": thread.id})





if __name__ == '__main__':
    app.run(debug=True)