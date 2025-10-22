# aliases: file

```bash
@file \
	[sudo] \
	replace \
	<filename> \
	--cat 1 \
	--save 0 \
	--this this-1+this-2 \
	--that that-1+that-2 \
	--whole_line 1
 . <this> -> <that> in <filename>.
@file \
	[-] \
	size \
	<filename> \
	--pretty 0
 . size of <filename>
```
