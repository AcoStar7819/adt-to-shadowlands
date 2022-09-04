from typing import Union

class Listfile:
    def __init__(self, path: str):
        self._data = {} # fileId: filePath
        with open(path, "r") as file:
            while (line := file.readline().rstrip()):
                id, path = line.split(';', 1)
                self._data[id] = path

    def getPath(self, id: int) -> Union[str, None]:
        '''
        Get path by file id
        '''
        id = str(id)
        if id in self._data:
            return self._data[id]
        return None

    def getId(self, path: str) -> Union[int, None]:
        '''
        Get file id by full path to file
        '''
        for id, value in self._data.items():
            if path == value:
                return id
        return None