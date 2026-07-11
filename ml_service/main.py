from flask import Flask, request, jsonify
from ssd_algorithm.py import speculative_decoding

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize():
    try:
        data = request.json
        input_text = data.get('input_text', '')
        max_tokens = data.get('max_tokens', 50)
        temperature = data.get('temperature', 1.0)
        top_k = data.get('top_k', 50)
        top_p = data.get('top_p', 0.9)

        # Run SSD algorithm
        generated_text = speculative_decoding(input_text, max_tokens, temperature, top_k, top_p)

        return jsonify({
            "input_text": input_text,
            "generated_text": generated_text,
            "tokens_generated": len(generated_text.split())
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
