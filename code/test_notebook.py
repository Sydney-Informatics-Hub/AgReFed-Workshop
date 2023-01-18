"""
Automating test script for notebook Data_Harvester.ipynb

This script is used to test the notebook in JupyterLab environment:
1) automatically unzips all scripts and folders on the user's JupyterLab environment (if not exists yet)
2) load test settings yaml file
3) runs Jupyter notebook
"""

import os
from pathlib import Path
import zipfile
import yaml
from datetime import datetime, timezone
# check if papermill is installed:
try:
    # for running Jupyter notebooks with cmd line arguments:
    import papermill as pm
except:
    os.system('pip install papermill')
    import papermill as pm


# Filename of zip file
zip_file = 'AgReFed-DataHarvester-main.zip'

# directory_to_extract_to:
directory_to_extract_to = './'

# path to notebook in zip file 
path_notebook = './AgReFed-DataHarvester-main/code/'

# name of notebook to test:
fname_notebook = 'Data_Harvest.ipynb'

# Settings file to load:
fname_settings = 'settings/settings_v0.2_testnotebook.yaml'


def unzip_file(zip_file, directory_to_extract_to):
    """
    Unzip file (helpful for installing latest repo as zip on JupyterLab)
    """
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

def runtest():
    """
    Run test notebook
    """
    # Change to notebook folder
    os.chdir(path_notebook)

    # date for notebook name
    date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    outfname = f'{Path(fname_notebook).stem}_{date}.ipynb'

    # Find output path in settings file
    #with open(fname_settings, 'r') as f:
    #    settings = yaml.load(f, Loader=yaml.FullLoader)
    #outpath = settings['outpath']

    # run notebook with papermill
    # Note: Need to add tag "parameters" in cell with load_settingsfilename in notebook first. 
    # (VS code has no tag option yet, so use text editor to tag cell)
    nb = pm.execute_notebook(
        fname_notebook, 
        outfname, 
        parameters = dict(load_settingsfilename = fname_settings))

    """
    # other ways to run notebook, some default ways:
    os.system('jupyter notebook ' + fname_notebook)
    #os.system("jupyter nbconvert --to notebook --execute " + fname_notebook)
    # or convert first to python script and then run:
    os.system(f'jupyter nbconvert {fname_notebook} --to python')
    """

def main():
    """
    Main function
    """
    # Unzip file

    unzip_file(zip_file, directory_to_extract_to)

    # Run notebook
    runtest()

if __name__ == '__main__':
    main()

