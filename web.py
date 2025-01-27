from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page (form input)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Get numbers from the form
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])

            # Perform operations
            sum_result = num1 + num2
            multiplication_result = num1 * num2
            division_result = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

            # Return the result to the user
            return render_template("index.html", sum_result=sum_result, 
                                   multiplication_result=multiplication_result, 
                                   division_result=division_result, 
             
