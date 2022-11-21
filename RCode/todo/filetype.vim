au BufWritePost	*.gv
   \ make -i -s | call feedkeys("\<Enter>")
au BufWritePost *.tex
   \ make -i -s | call feedkeys("\<Enter>")
au BufWritePost *.lst
   \ make -i -s | call feedkeys("\<Enter>")
