import abc
import os

class OperatingSystem(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def data_filepath():
        # This should point to the folder where the actual data entry logs, the .csv and .json files, are stored.
        pass

    @abc.abstractmethod
    def repopath():
        # This should point to the folder root, which should contain the .git folder.
        pass

# TODO For whichever devices from which you run the data entry script, set the path that points to the relevant folders
class Android(OperatingSystem):

    def data_filepath():
        return os.path.expanduser("~/scripts/mylogs/lifedata/{0}")
    def repopath():
        return os.path.expanduser("~/scripts/mylogs")

class Windows(OperatingSystem):

    def data_filepath():
        return "c:/Users/username/dataentry/lifedata/{0}"
    def repopath():
        return "./"

class Ubuntu(OperatingSystem):

    def data_filepath():
        return os.path.expanduser("~/projects/personal-logs/mylogs/lifedata/{0}")

    def repopath():
        return "./"