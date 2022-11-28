# ADT converter from 3.3.5 to 9.1.5
A small Python script that can help you convert adt files from 3.3.5 to 9.1.5 (maybe nearest versions also work, I haven't tested this).

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

## Known Issues
### Converter crash at "Converting adt..." stage.
This usually happens when you converting adt that have downgraded to LK. The Luzifix converter can break if it see chunks that are not intended for 335.

The most common chunk that causes this problem is [MCLV](https://wowdev.wiki/ADT/v18#MCLV_sub-chunk_.28Cata.2B.29).

Python script should automatically remove MCLV. Make sure the line "remove_mclv=true" is exist in config.txt

If the problem persists, compile [Luzifix ADT Converter](https://github.com/Luzifix/ADTConvert) from sources and debug it to find the problem causing the error.
### Landscape LOD bug like [this](https://i.imgur.com/Ad3bdfe.mp4) (Only for continents, I think).
A full LOD update for the new landscape would be a good solution, but there is an easier and time-saving option.

Take [WDT](https://wowdev.wiki/WDT#MPHD_chunk) file from your shadowlands client and edit it using 010 editor.

You will need to remove the flag 0x0100 and 0x8000 (if exists). This will disable use of lod files. Draw distance will drop to 335.

You also can use [this fixer](https://github.com/AcoStar7819/wdt-flags-fixer) to do it automatically and faster.
