from flask import Flask, render_template, request, redirect, url_for, send_from_directory, current_app, make_response
from werkzeug.utils import secure_filename
import os
import subprocess as sp

FFMPEG_BIN = "ffmpeg.exe"

# Statics
UPLOAD_FOLDER = 'files\\uploaded'
DOWNLOAD_FOLDER = 'files\\download'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'ogg', 'flac'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

def allowed_file(filename):
	# Build the filename + extension after checking if allowed
	# Note: \ == explicit line continuation
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']

		# check if the post request has the file part
		if 'file' not in request.files or file.filename == '':
			return redirect(url_for('home'))

		if file and allowed_file(file.filename):

			# Server-side check to prevent client-side value manipulation
			format = request.form.get("format_select")
			if str(format) in ALLOWED_EXTENSIONS:
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

				# Convert
				dfile = '{}.{}'.format(os.path.splitext(filename)[0], str(format)) # Build file name
				inputF = os.path.join(app.config['UPLOAD_FOLDER'], filename) # Build input path
				outputF = os.path.join(app.config['DOWNLOAD_FOLDER'], dfile) # Build output path and add file
				convertCMD = [FFMPEG_BIN, '-y', '-i', inputF, outputF] # Ffmpeg is flexible enough to handle wildstar conversions

				executeOrder66 = sp.Popen(convertCMD)

				try:
					outs, errs = executeOrder66.communicate(timeout=5) # tell program to wait
				except TimeoutError: # Kill if it takes too long
					proc.kill()
				print("DONE\n")

				# Send as a downloadable file
				ddir = os.path.join(current_app.root_path, app.config['DOWNLOAD_FOLDER'])
				return send_from_directory(directory=ddir, filename=dfile, as_attachment=True)

		return render_template('home.html')
	else:
		return redirect(url_for('home'))

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
