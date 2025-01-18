
# Universal Translator 🌐

A Flask-based multilingual translation app leveraging open-source large language models (LLMs) to translate text seamlessly between over 100 languages, including English, Urdu, Japanese, Korean, and more. This project uses Hugging Face's `transformers` library and `facebook/m2m100_418M` model to deliver accurate translations.

## 🌟 Features
- Translate text between 100+ languages.
- Supports languages like English, Urdu, Japanese, Korean, Spanish, Hindi, and French.
- Detects input language automatically (optional).
- Clean and user-friendly interface.
- Open-source and customizable.


## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Model**: Hugging Face's `facebook/m2m100_418M`
- **Libraries**: `transformers`, `torch`, `langdetect`


## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Pip (Python package manager)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/universal-translator-llm.git
   cd universal-translator-llm
   ```

2. **Set Up a Virtual Environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the App**
   Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).


## 🌍 Supported Languages
The project supports over 100 languages. Some key ones include:
- **English (en)**
- **Urdu (ur)**
- **Japanese (ja)**
- **Korean (ko)**
- **Hindi (hi)**
- **French (fr)**
- **Spanish (es)**

For a full list of supported languages, refer to the [M2M100 documentation](https://huggingface.co/facebook/m2m100_418M).


## 🖼️ User Interface
The app features a clean and simple web UI:
- Input the text you want to translate.
- Select source and target languages from the dropdowns.
- Click "Translate" to see the results instantly.


## ✨ Project Structure
```
universal-translator-llm/
├── static/
│   ├── styles.css       # Custom CSS for UI styling
├── templates/
│   ├── index.html       # Main HTML file
├── app.py               # Flask app with translation logic
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

## 🔧 Configuration

### Adding New Languages
To add new languages, update the `index.html` file's dropdown with the desired language code and name:
```html
<option value="ur">Urdu</option>
<option value="ja">Japanese</option>
<option value="ko">Korean</option>
```


## 🤝 Contributing
Contributions are welcome! If you want to improve the app or add new features:
1. Fork the repository.
2. Create a new branch.
3. Make your changes and submit a pull request.
