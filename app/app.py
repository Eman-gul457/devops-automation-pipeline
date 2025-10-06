from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Deployment</title>
        <style>
            body {
                font-family: 'Inter', 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #f8f9fb, #e8ecf3);
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #333;
            }
            .card {
                background: #ffffff;
                padding: 40px 50px;
                border-radius: 18px;
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
                text-align: center;
                max-width: 450px;
            }
            h1 {
                font-size: 1.4rem;
                margin-bottom: 10px;
                color: #2c3e50;
                letter-spacing: 0.5px;
            }
            p {
                font-size: 0.95rem;
                color: #666;
                margin-top: 8px;
            }
            .emoji {
                font-size: 1.5rem;
                display: inline-block;
                margin-left: 5px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Flask App Deployed Successfully<span class="emoji">🚀</span></h1>
            <p>via Jenkins + Ansible + Docker</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
                                         
