from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This route returns info about the food
@app.route('/SUBMITDATA/', methods=['POST'])
def submit_data():
    print("HAPPENING")
    #calls the corresponding API here
    image = request.files['image']
    pref = request.form.get('image')

    return {
        "foods_identified": ["celery", "lettuce", "tomato", "crutons"], 
        "recipe": "Can create salad",
        "calories": 1000,
        "protein": 1000,
        "carbs": 500, 
        "fats": 300,
        "sugar": 100
    }
    return "201"
    
if __name__ == "__main__":
    app.run(debug = True)