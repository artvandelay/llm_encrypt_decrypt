from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Path to the ts_sms binary
TS_SMS_BINARY = "./ts_sms-2024-12-26/ts_sms"

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get("text", "")
    try:
        # Call the ts_sms binary for encryption
        result = subprocess.run(
            [TS_SMS_BINARY, "c", text],
            capture_output=True,
            text=True,
        )
        return jsonify({"result": result.stdout.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    text = data.get("text", "")
    try:
        # Call the ts_sms binary for decryption
        result = subprocess.run(
            [TS_SMS_BINARY, "d", text],
            capture_output=True,
            text=True,
        )
        return jsonify({"result": result.stdout.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
