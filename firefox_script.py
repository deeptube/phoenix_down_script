import os
import shutil
from constants import *
from utilities import *


# VARIABLES ------------------------------------------------------------------------------------------------------------

application_name = "firefox"


# SCRIPT ---------------------------------------------------------------------------------------------------------------


def firefox_script():
    # If the work directory "../trello" doesn't existe yet...
    # ... creation of this directory
    create_directory(PD_SCRIPT_FIREFOX_DIRECTORY_PATH)

    # Designation of firefox profile directory as current directory
    os.chdir(FIREFOX_PROFILE_DIRECTORY_PATH)

    # copying local places.sqlite (firefox profile) to phoenix down script / firefox directory
    shutil.copy(FIREFOX_PLACES_SQLITE_FILE_NAME, PD_SCRIPT_FIREFOX_DIRECTORY_PATH)

















# TODO : save + upload du fichier places.sqlite (BDD des bookmarks, DL et historique)
# TODO : si possible, parcourir le dossier bookmarkbackups et grap le fichier le plus récent (save au format JSON, chiffré)
# TODO : récupérer aussi favicons.sqlite
# TODO : comme le nommage des fichiers ne peut pas être horodaté (intégrité pour éventuel import), créer des dossiers horodatés