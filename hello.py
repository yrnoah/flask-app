from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('hello'))

# 尾部url/使url访问可以重定向，访问不带斜线的url可以重定向到带/的
@app.route('/hello')
def hello():
    return render_template('hello.html', name="noah")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

# with app.test_request_context():
#     print url_for('index')
#     print url_for('hello')
