from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# تعريف تطبيق Flask
app = Flask(__name__)

# مفتاح Hugging Face (يمكنك استخدام مفتاحك الخاص)
API_KEY = "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"

# تهيئة نموذج توليد الأسئلة
question_generator = pipeline("question-generation", model="valhalla/t5-small-qa-qg-hl", token=API_KEY)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_questions", methods=["POST"])
def generate_questions():
    # استخراج النص من الطلب
    text = request.json.get("text")
    
    # توليد الأسئلة باستخدام Hugging Face
    questions = question_generator(text)
    
    # إرجاع الأسئلة كـ JSON
    return jsonify(questions)
