from flask import Flask, send_file, render_template
import zipfile

from helpers.data_read_write import flattened_exercise_to_csv

app = Flask(__name__, template_folder='view')

@app.route('/')
def home():
    """Print 'Hello, world!' as the response body."""
    return render_template('home.html')

@app.route('/download_csv')
def download_csv():
    """Downloads a csv and data map to represent flattened current sqlite database."""
    csv_paths = flattened_exercise_to_csv()
    zip_file_name = 'sqlite_output.zip'
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(csv_paths.csv)
        zip_file.write(csv_paths.data_map)

    return send_file(zip_file_name, mimetype='application/zip', as_attachment=True)

@app.route('/data-exploration')
def data_exploration():
    return render_template('data_exploration.html')


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


