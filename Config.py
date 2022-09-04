from typing import Union

class Config:
    def __init__(self, path: str):
        self._settings = {}
        with open(path, "r", encoding="UTF-8") as config:
            lines = config.readlines()
            for line in lines:
                line = line.replace(b"\xEF\xBB\xBF".decode("UTF-8"), "") # UTF-8 with BOM
                if line.startswith("#"):
                    continue
                if (line == "") or (line == " ") or (line == "\n"):
                    continue
                try:
                    line = line.strip()
                    line = line.split("=")
                    line[0] = line[0].lower()
                    self._settings[line[0]] = line[1]
                except:
                    print(f"Error while loading config.txt\n{line}")

        Config._instance = self
    
    def get(self, key: str, default_value: str = None) -> Union[str, None]:
        if key in self._settings:
            return self._settings[key]
        return default_value