# Text Information
The text of the games is held in script.cpk and in the MES files.  The files are in Shift-Jis (cp932).
The formats allow for three lines per text box.  Each text box has a length of 0x90, so each line allows for 0x30 bytes.
The reason you need to use full length alphanumeric characters is because the game reads how many bytes there are and divides it by two to decide how many characters to display.  If you were to use ASCII characters, it would read all the bytes and divide it by two, as it is expecting SJIS characters, which are two bytes. (Hopefully that made sense)
# Image Information
These files are in little endian.
The first two bytes are the the texture type.  The next 2 bytes are the width, and the next two bytes after that are the height. The next two bytes are unknown.
# Texture Type 3
The texture starts at 0x10.  It is ABGR4444.  It has a swizzle, the exact same as the NDS. 
# Texture Type 9
This is a pallete format.  The pallete starts at 0x10. There is 8 bits per index, and an unknown pallete encoding (although it is more than likely some sort of a 2 byte RGBA encoding).  The actual index starts at 0x210.  There could possibly be a swizzle here, although I don't know for certain.
# Other
MOST of the rest of the file are known formats and Google will help with you with that.
