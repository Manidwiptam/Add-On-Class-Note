from flask import Flask, render_template
from student import Student ,Details

app=Flask(__name__)

students= [
        Student("Manidwiptam Halder", "N/A", "CSE - B"),
        Student("Rahidul Khan", "16", "CSE - a"),
        Student("Zahir Ali", "79", "CSE - B"),
        Student("Neel", "41", "CSE - A"),
        Student("Biman Roy", "75", "CSE - B"),
        Student("Sristi", "N/A", "CSE - B"),
        Student("Nagma", "N/A", "CSE - B")
    ]

student_details_data = {
        "Manidwiptam Halder": Details("998xxxxx", "Kalyani", "M"),
        "Rahidul Khan": Details("997xxxxx", "Kolkata", "M"),
        "Zahir Ali": Details("996xxxxx", "Howrah", "M"),
        "Neel": Details("995xxxxx", "Delhi", "M"),
        "Biman Roy": Details("994xxxxx", "Durgapur", "M"),
        "Sristi": Details("993xxxxx", "Kalyani", "F"),
        "Nagma": Details("992xxxxx", "Kolkata", "F")
    }

@app.route("/students")
def studentdetails():
    return render_template("index.html", students=students)

@app.route("/student/<name>")
def student_details(name):
    detail = student_details_data.get(name)
    return render_template("data.html", name=name, detail=detail)

if __name__ == "__main__":
    app.run(debug=True)

