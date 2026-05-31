from flask import Flask, request, jsonify, send_from_directory
import tiktoken

app = Flask(__name__, static_folder="static")

ENCODINGS = {
    "gpt2":       "gpt2",
}

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/tokenize", methods=["POST"])
def tokenize():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    model_key = data.get("model", "gpt2")

    if not text:
        return jsonify({
            "tokens": [],
            "ids": [],
            "stats": {
                "total": 0,
                "unique": 0,
                "chars": 0,
                "words": 0,
                "lines": 0,
                "avg_len": 0,
                "top": [],
                "repeated": 0,
                "longest": "",
            },
        })

    enc_name = ENCODINGS.get(model_key, "gpt2")
    enc = tiktoken.get_encoding(enc_name)

    ids = enc.encode(text)
    tokens = [
        enc.decode_single_token_bytes(i).decode("utf-8", errors="replace")
        for i in ids
    ]

    # Stats
    freq = {}
    for t in tokens:
        clean = t.strip()
        if clean:
            freq[clean] = freq.get(clean, 0) + 1

    visible_tokens = [t for t in tokens if t.strip()]
    top_tokens = sorted(freq.items(), key=lambda x: (-x[1], x[0].lower()))[:10]

    stats = {
        "total":    len(tokens),
        "unique":   len(set(t.strip() for t in visible_tokens)),
        "chars":    len(text),
        "words":    len(text.split()),
        "lines":    text.count("\n") + 1,
        "avg_len":  round(sum(len(t) for t in visible_tokens) / max(len(visible_tokens), 1), 1),
        "top":      top_tokens,
        "repeated": sum(1 for count in freq.values() if count > 1),
        "longest":  max(visible_tokens, key=len) if visible_tokens else "",
    }

    return jsonify({"tokens": tokens, "ids": list(ids), "stats": stats})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
