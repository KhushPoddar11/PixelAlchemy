from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
from convert import converter
from TextExtract import extracting
from lightEnhancement import lowLight
from merge import merger, image1, image2
import cv2
import os
from blur import deblur

UPLOAD_FOLDER = 'static/input'
ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
# app = Flask(__name__, static_url_path='/outputs')
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("extract.html")

@app.route("/extract")
def extract():
    return render_template("extract.html")

@app.route("/enhance")
def enhance():
    return render_template("enhance.html")

@app.route("/mergePage")
def mergePage():
    return render_template("merge.html")

@app.route("/deblurPage")
def deblurPage():
    return render_template("deblur.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST": 
        operation = request.form.get("operation")
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "error no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            converter(filename)
            return render_template("index.html")

    return render_template("index.html")

@app.route("/extractText",methods=["GET","POST"])
def extractText():
    if request.method == "POST": 
        operation = request.form.get("operation")
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "error no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            text = extracting(filename)
            return render_template("ui4.html", filename=filename, text=text)

@app.route("/enhanceImage",methods=["GET","POST"])
def enhanceImage():
    if request.method == "POST": 
        operation = request.form.get("operation")
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "error no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            lowLight(filename)
            return render_template("ui2.html", filename=filename)
        
@app.route("/merge",methods=["GET","POST"])
def mergeImage():
    if request.method == "POST": 
        operation = request.form.get("operation")
        if 'file' not in request.files or 'file1' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        file1 = request.files['file1']
        if file.filename == '' and file1.filename=='':
            flash('No selected file')
            return "error no selected file"
        if file and file1 and allowed_file(file.filename) and allowed_file(file1.filename):
            filename = secure_filename(file.filename)
            filename1 = secure_filename(file1.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            image1(filename)
            image2(filename1)
            merger()
            return render_template("showMerged.html")

@app.route("/deblur",methods=["GET","POST"])
def deblurImage():
    if request.method == "POST": 
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "error no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            deblur(filename)
            return render_template("ui3.html", filename=filename)


app.run(debug=True, port=5009)