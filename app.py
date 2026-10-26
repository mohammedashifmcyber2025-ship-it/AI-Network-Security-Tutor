from flask import Flask, request

app = Flask(__name__)

topics = {
    "firewall": "A firewall filters network traffic according to security rules.",
    "encryption": "Encryption converts readable data into a protected, unreadable form.",
    "phishing": "Phishing tricks people into revealing passwords or sensitive information.",
    "malware": "Malware is harmful software, including viruses and ransomware.",
    "authentication": "Authentication verifies a user's identity.",
    "cryptography": "Cryptography protects information using encryption, hashing, and digital signatures.",
    "ids": "An IDS detects suspicious activity and generates alerts.",
    "ips": "An IPS can detect and block malicious network traffic.",
    "vpn": "A VPN creates an encrypted connection to a VPN endpoint.",
    "cia triad": "The CIA triad means Confidentiality, Integrity, and Availability."
}


@app.route("/", methods=["GET", "POST"])
def home():
    question = ""
    answer = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip().lower()

        if question:
            for topic, explanation in topics.items():
                if topic in question:
                    answer = explanation
                    break

            if not answer:
                answer = (
                    "I don't know that topic yet. Try asking about "
                    "firewall, encryption, phishing, malware, "
                    "authentication, cryptography, IDS, IPS, VPN, "
                    "or the CIA triad."
                )
        else:
            answer = "Please enter a question."

    topic_list = ""

    for topic, explanation in topics.items():
        topic_list += f"<h3>{topic.upper()}</h3><p>{explanation}</p>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Network Security Concepts Tutor</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #eef3f8;
                color: #1e293b;
                margin: 0;
                line-height: 1.6;
            }}
            header {{
                background: #102a43;
                color: white;
                padding: 25px;
                text-align: center;
            }}
            main {{
                max-width: 900px;
                margin: 25px auto;
                padding: 15px;
            }}
            section {{
                background: white;
                padding: 22px;
                margin-bottom: 20px;
                border-radius: 12px;
                box-shadow: 0 3px 10px #00000010;
            }}
            input[type="text"] {{
                width: 70%;
                padding: 12px;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
            }}
            button {{
                background: #1769aa;
                color: white;
                padding: 12px 18px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }}
            .answer {{
                background: #e0f2fe;
                padding: 15px;
                border-radius: 8px;
            }}
            .topic {{
                border-bottom: 1px solid #e2e8f0;
                padding: 10px 0;
            }}
            footer {{
                text-align: center;
                padding: 20px;
                color: #64748b;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>AI Network Security Concepts Tutor</h1>
            <p>Your beginner-friendly cybersecurity learning platform</p>
        </header>
        <main>
            <section>
                <h2>Ask Your Tutor</h2>
                <form method="POST">
                    <input type="text" name="question"
                        placeholder="Example: What is a firewall?"
                        value="{question.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace(chr(34), '&quot;')}"
                        required>
                    <button type="submit">Ask</button>
                </form>
                <h3>Tutor's Answer</h3>
                <div class="answer">{answer.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')}</div>
            </section>
            <section>
                <h2>Network Security Learning Modules</h2>
                {topic_list}
            </section>
        </main>
        <footer>
            AI Network Security Concepts Tutor | Educational Project
        </footer>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True)