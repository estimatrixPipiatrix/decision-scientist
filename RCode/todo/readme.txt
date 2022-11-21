to install:

(1) make sure that R,ImageMagick,vim and make are
    all installed

(2) copy filetype.vim into the .vim directory located
    in your home directory if the file does not already
    exist; if it does already exist then just add the
    contents of this file to the end of that one

to use, open todo.lst with vim from the bash shell; 
when you save the file, make will run status.sh, which
will in turn display a progress bar
