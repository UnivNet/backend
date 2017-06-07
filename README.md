# UnivNet backend

### Get started

- Fork & clone this repository
- Install [anaconda](https://www.continuum.io/downloads) or [miniconda](https://conda.io/miniconda.html)
- Navigate to the root of your local repository and type `conda env create -f environment.yml`
    - This will create a virtual env `UnivNet_env` with all necessary packages installed
- If using PyCharm (preferably), _change your project interpreter_ to this virtual environment, otherwise,
 [activate the environment](https://conda.io/docs/using/envs.html#change-environments-activate-deactivate) 
 from terminal.
- You'll **also** need the `.env` file to access the project settings
    - Get it from the Google Drive
    - Place it in the project root
    - Be _responsible_, handle the `.env` file like you'd handle your passwords
    - An example env file is provided at `.env.example`


### Quick help
- [Python Decouple docs](https://pypi.python.org/pypi/python-decouple)
- [Delete superuser](https://stackoverflow.com/a/26713562/4626943)
- Remove a conda environment `conda env remove -n [name_of_env]`
