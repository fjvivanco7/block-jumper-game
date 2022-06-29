import glob
import io
import os
import uuid

import numpy as np
from flask import Flask, jsonify, make_response, render_template, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
app.secret_key = "1726463548"
app._static_folder = os.path.abspath("templates/")


@app.route("/", methods=["GET"])
def index():
    title = "Create the input image"
    return render_template("index.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)