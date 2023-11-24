from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return "Explore my exciting projects here!"

@app.route('/about')
def about():
    return "Learn more about me and my DevOps journey."

@app.route('/contact')
def contact():
    return "Feel free to reach out to me! Phone: +1 (555) 123-4567, Email: info@example.com"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



