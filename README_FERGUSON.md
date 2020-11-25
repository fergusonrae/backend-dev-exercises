
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
