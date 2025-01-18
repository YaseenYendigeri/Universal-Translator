from flask import Flask, render_template, request, jsonify
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


app = Flask(__name__)

# Load the translation model and tokenizer
MODEL_NAME = "facebook/m2m100_418M"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Parse the request
        source_text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        # Tokenize the input
        tokenizer.src_lang = source_lang
        encoded_text = tokenizer(source_text, return_tensors="pt")

        # Generate translation
        translated_tokens = model.generate(**encoded_text, forced_bos_token_id=tokenizer.lang_code_to_id[target_lang])
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
