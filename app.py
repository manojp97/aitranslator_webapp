from flask  import Flask, render_template, request
from transformers import MarianMTModel, MarianTokenizer
app = Flask(__name__)

# to select the model

model_name = "Helsinki-NLP/opus-mt-en-hi"

# to load the modelfrom flask import Flask, render_template, request
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

# Model name
model_name = "Helsinki-NLP/opus-mt-en-hi"

# Load model and tokenizer
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translation(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    result = tokenizer.decode(translated[0], skip_special_tokens=True)
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""

    if request.method == 'POST':
        data = request.form.get('data')  # safer way
        if data:
            translated_text = translation(data)

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)

model = MarianMTModel.from_pretrained(model_name)

# to load the tokenizer
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translation(text):
    # convert the text into token
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    # translate the data using model
    translated = model.generate(**inputs)
    # decode the token into readable text
    result = tokenizer.decode(translated[0], skip_special_tokens=True)
    return result

@app.route('/', methods=['POST','GET'])
def index():
        translated_text = ""
        if request.method == 'POST':
            data = request.form['data']
            translated_text = translation(data)
        return render_template('index.html', translated_text=translated_text)

    # return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)