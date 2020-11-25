
# Directory

- `data`: Static datasets used for analysis
- `doc`: Contains diagram used to structure project
- `helpers`: Folder of functions and test to collect information for the app.
- `notebook`: Folder containing cleared Jupyter notebook code
- `view`: Dir of front end html files
- `.editorconfig`: Automatically corrects project to certain standards around spacing and line endings
- `.pylintrc`: Defines code standards for python for linting
- `app.py`: Script to start UI
- `conftest.py`: Configuration file for pytest. Defines project-wide fixtures.
- `environment.yml`: Conda env file

# Setup
Create environment with conda
```shell
conda create -n rti_project -f environment.yml
```

Use .editorconfig
- PyCharm: No additional steps needed
- VSCode: Download `editorconfig` extension and restart program

# Run through Terminal
```shell
conda activate rti_project
flask run
```

# Run Tests
```shell
conda activate rti_project
pytest
```


# Next Steps
- Project
    - Collect desired focus of application
        - One-time analysis of data?
        - Assist user in selecting and training models?
- Front End
    - More aesthetically friendly UI
    - Feature: paginated view of data
    - Feature: ability for user to query db and return results
- Data Cleaning
    - Handling of missing data ('?')
    - Keep one of `grades_completed` and `education_num`
- Data Analysis
    - Run dataset through automl library to pull out potential predictors
- Backend
    - Hook that saves then clears nb output on push to repo to avoid large deltas in git history
    - Create pytest fixture to recreate desired pandas dataframe in `test_data_read_write.py` for each function
    - Rethink naming of files.
        - ex, should `constants.py` be `sql_scripts.py`?
