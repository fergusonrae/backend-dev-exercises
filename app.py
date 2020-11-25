from flask import Flask, send_file, render_template, request
import zipfile

from helpers.data_read_write import flattened_exercise_to_csv, flattened_exercise, csv_to_dataframe
from helpers.model import SavedCSV
from helpers.paths import SAVED_CSV_PATH, SAVED_DATA_MAP

app = Flask(__name__, template_folder='view')

TMESTAMPED_SQLITE_DATA = csv_to_dataframe(SavedCSV(csv=SAVED_CSV_PATH, data_map=SAVED_DATA_MAP))

@app.route('/')
def home():
    """main page."""

    return render_template('home.html')

@app.route('/paginated-data')
def paginated_data():
    """Return sqlite flattend data as a series of pages."""
    # Set the pagination configuration
    page = request.args.get('page', 1, type=int)

    num_entriees_per_page = 10
    paged_data = TMESTAMPED_SQLITE_DATA[(page-1)*num_entriees_per_page: num_entriees_per_page*page]
    return render_template('paginated_data.html', sqlite_data=paged_data)


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


