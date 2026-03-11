from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')


@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])

    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)

    return render_template(
        "caesar.html",
        encrypt_result=encrypted_text,
        plain_text=text,
        key=key
    )


@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])

    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)

    return render_template(
        "caesar.html",
        decrypt_result=decrypted_text,
        cipher_text=text,
        key=key
    )


# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8686, debug=True)