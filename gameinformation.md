# Text Information
The text of the game is held in script.cpk and in the MES files.  The files are in Shift-Jis (cp932).
The formats allow for three lines per text box.  Each text box has a length of 0x90, so each line allows for 0x30 bytes.
The reason you need to use full length alphanumeric characters is because the game reads how many bytes there are and divides it by two to decide how many characters to display.  If you were to use ASCII characters, it would read all the bytes and divide it by two, as it is expecting SJIS characters, which are two bytes. (Hopefully that made sense)
# Image Information 
The images of the game are held in graph.cpk and in the PSP files.
[This plugin](https://github.com/SamuraiOndo/various-noesis-plugins/blob/main/ano_psp.py) for [Noesis](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91) for all of the image formats.
# Other
MOST of the rest of the file are known formats and Google will help with you with that.
