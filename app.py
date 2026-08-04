from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai-image')
def ai_image():
    return render_template('ai_image.html')

@app.route('/qr-generator')
def qr_generator():
    return render_template('qr_generator.html')

@app.route('/ai-video')
def ai_video():
    return render_template('ai_video.html')

@app.route('/ai-voice')
def ai_voice():
    return render_template('ai_voice.html')

# Demo API - ابھی test کے لیے
@app.route('/api/generate', methods=['POST'])
def generate():
    tool = request.form.get('tool')
    prompt = request.form.get('prompt')
    return jsonify({"status": "success", "message": f"{tool} tool is ready! Prompt: {prompt}"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
