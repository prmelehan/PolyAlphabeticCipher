# PolyAlphabeticCipher
A Polyalphabetic Cipher created using python.
## Requirements:
<a href='https://python.org'>Python >= 3</a>

## Usage
<code>python3 /path/to/encodeordecode/python/file.py</code>

For example if I was on an Apple Computer and the files were on my Desktop:

<code>python3 /Users/"myusername"/Desktop/enc.py</code>

Follow built in instructions and you should be all set.

#### For ease of use:

Place the de-enc.py and enc.py at your home folder or another place where you keep code, then edit .bashrc (Linux) or .bash_profile (Mac) and add:
<code>alias encode="python3 /path/to/encode/python/file.py"</code>

Source your .bashrc or .bash_profile and you're good. Do the same for the decode file; Add a new alias for the decode just as you did for the encode

##### Now for a full example:

If the de-enc.py and enc.py are in a users home folder on Mac:
<code>cd; nano .bash_profile</code>

Add:

<code>alias encode="python3 /Users/username/enc.py"</code>

<code>alias decode="python3 /Users/username/de-enc.py"</code>

Save, then source:

<code>source .bash_profile</code>

If the de-enc.py and enc.py are in a users home folder on Linux:

<code>cd; nano .bashrc</code>

Add:

<code>alias encode="python3 /home/username/enc.py"</code>

<code>alias decode="python3 /home/username/de-enc.py"</code>

Save, then source

<code>source .bashrc</code>

## Additional Characters

Additional characters can be added by simply adding them to the PolyDictA dictionary in both files. Following the standards put in place. Ex: 'letter':'number'

Emoji and other characters could be added. One must also increase the modular count. At every instance in both files, 'replace % 85' with '% int of amt of characters'. In order to find the amount of total characters PolyDict has, add one to the last number you see. By default, the last number is 84, so the number our modular needs to be is 85. 84 + 1 = 85.

The script is fairly well commented and should be easily understandable.
