from flask import Flask,request

flask = Flask(__name__)

@flask.route('/')
def home():
    return '''Hello!This is the Homepage \n 
            To change your string to Uppercase GOTO:  /toUpper?str=Your_String   //OR//  
            To capitalize your string GOTO:  /capital?str=Your_String
            '''

@flask.route('/toUpper')
def toUpper():
    query=request.args.get('str')
    return query.upper()

@flask.route('/capital')
def capital():
    query=request.args.get('str')
    return query.capitalize()

if __name__ == '__main__':
    flask.run(debug=True)