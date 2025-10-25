from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from google import genai

app = Flask(__name__)
CORS(app)

# Read API key from env var GOOGLE_API_KEY or from a file if you prefer
API_KEY = os.environ.get("GOOGLE_API_KEY", None)

if not API_KEY:
    print("WARNING: GOOGLE_API_KEY not set. Set it before running in production.")

# Create genai client (Gemini)
client = genai.Client(api_key=API_KEY)

# Choose model — you can change to gemini-2.5-flash, gemini-1.5, etc.
MODEL = os.environ.get("GENAI_MODEL", "gemini-2.5-flash")

@app.route("/ai", methods=["POST"])
def ai():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"result": "Tolong masukkan pertanyaan!"}), 400

    try:
        # Use the Google Gen AI SDK to generate content
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        # response.text should contain the generated text
        text = getattr(response, "text", None) or str(response)
        return jsonify({"result": text})
    except Exception as e:
        return jsonify({"result": f"Error calling Gemini API: {str(e)}"}), 500

if __name__ == "__main__":
    # Render/hosting platforms expect to listen on 0.0.0.0 and a port from env
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
