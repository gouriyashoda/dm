def reilfence_encrypt(text, rails):
    fence = [[''] * len(text) for _ in range(rails)]
    rail, direction = 0, 1

    for char in text:
        fence[rail][len(fence[rail]) - len(text)] = char
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return ''.join(''.join(row) for row in fence)


def reilfence_decrypt(cipher_text, rails):
    fence = [[''] * len(cipher_text) for _ in range(rails)]
    rail, direction = 0, 1

    for i in range(len(cipher_text)):
        fence[rail][i] = '*'
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if fence[i][j] == '*':
                fence[i][j] = cipher_text[index]
                index += 1

    plain_text = ''
    rail, direction = 0, 1
    for i in range(len(cipher_text)):
        plain_text += fence[rail][0]
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return plain_text

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        rails = int(request.form['rails'])
        action = request.form['action']

        if action == 'encrypt':
            result = reilfence_encrypt(text, rails)
        elif action == 'decrypt':
            result = reilfence_decrypt(text, rails)
        else:
            result = "Invalid action"

        return render_template('index.html', result=result, text=text, rails=rails)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
