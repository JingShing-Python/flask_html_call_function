from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    result = 'Function in Flask has been called'
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
