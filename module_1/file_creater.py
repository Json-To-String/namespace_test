import os

class FileCreator:
    def create(filename: str):
        path_exists = os.path.exists(filename)
        if not path_exists:
            os.makedirs(filename)
        else:
            print(f"Something went wrong trying to make {filename}")