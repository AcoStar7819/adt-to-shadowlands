# ADT converter from 3.3.5 to 9.0.5
A small Python script that can help you convert adt files from 3.3.5 to 9.0.5 (maybe later versions also work, I haven't tested this).

To do part of the work, the script uses two other converters:
- [Luzifix ADT Converter](https://github.com/Luzifix/ADTConvert) - For base adt fixing
- [Varen ADT Optimizer](https://github.com/Varen/WoW-ObjX.adt-Optimizer_735) - For models fixing

The binaries for these converters are included in the release of the script, but not in the source code.

The main work of the script is replacing texture paths with their id and automatically transfer files between converters.

## Usage
You will probably need CASCHost or Arctium to upload files into game.
### Compiled binaries
- Download latest compiled release
- Unpack archive into empty folder
- Put your adt files to the "input" folder
- Run "Convert.exe"
- Take converted files from "output" folder
### OR run source code
- Create the following folders in the project root directory:
  - "input" (You can change this folder location in config.txt)
  - "output" (You can change this folder location in config.txt)
  - "tools"
- Download listfile from [WoW.tools](https://wow.tools/) and place it in the project root directory (You can change this file location in config.txt)
- Download compiled ADTConvert.exe [from Luzifix repo](https://github.com/Luzifix/ADTConvert/releases) and place it into "tools" folder
- Create "optimizer" folder in "tools"
- Download compiled Obj_Optimizer_7x.exe [from Varen repo](https://github.com/Varen/WoW-ObjX.adt-Optimizer_735/releases) and unpack all files into "optimizer" folder
- Run "app.py" as python file

You can compile this with [PyInstaller](https://pyinstaller.org/en/stable/)
```
pyinstaller.exe --onefile --icon=app.ico app.py
```
