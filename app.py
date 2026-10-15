from flask import Flask, request, render_template_string
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")
NAMES = ["Setosa", "Versicolor", "Virginica"]

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ML App on AWS</title>
<style>
body{font-family:Arial,sans-serif;background:#eef2f7;text-align:center;padding:60px 20px}
.card{max-width:500px;margin:auto;padding:35px;background:#fff;border-radius:12px;box-shadow:0 4px 16px #0002}
h1{color:#1565c0}
input{margin:6px;padding:10px;width:80%;box-sizing:border-box}
button{padding:10px 26px;background:#1565c0;color:#fff;border:0;border-radius:6px;cursor:pointer}
.result{color:#2e7d32}
</style>
</head>
<body>
<div class="card">
  <h1>Iris Flower Predictor</h1>
  <p>ML + Docker + GitHub + CodePipeline + CodeDeploy</p>
  <p>Version: 1.0</p>
  <form method="post">
    <input name="sl" type="number" step="any" placeholder="Sepal length (cm)" required><br>
    <input name="sw" type="number" step="any" placeholder="Sepal width (cm)" required><br>
    <input name="pl" type="number" step="any" placeholder="Petal length (cm)" required><br>
    <input name="pw" type="number" step="any" placeholder="Petal width (cm)" required><br>
    <button type="submit">Predict</button>
  </form>
  {% if result %}<h2 class="result">Prediction: {{ result }}</h2>{% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        values = [float(request.form[k]) for k in ("sl", "sw", "pl", "pw")]
        result = NAMES[int(model.predict(np.array([values]))[0])]
    return render_template_string(PAGE, result=result)

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
