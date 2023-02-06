from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations':util.get_location_names()
    })

    response.headers.add('Access_Control_Allow_Origin','*')
    return response
    return "hi"


if __name__ == "__main__":
    print("starting python flsk")
    app.run()