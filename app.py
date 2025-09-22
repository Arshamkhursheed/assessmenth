from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])   # Homepage handles GET and POST
def home():
    result = None
    if request.method == "POST":    # If form submitted
        num1 = request.form.get("num1")   # Take first number from input
        num2 = request.form.get("num2")   # Take second number from input
        
        # Convert to integers and add
        result = int(num1) + int(num2)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
