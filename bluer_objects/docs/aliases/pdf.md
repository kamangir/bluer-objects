# aliases: pdf

```bash
@pdf \
	convert \
	[inline,combine,~compress,filename=<release.pdf>,install,upload] \
	<module-name> \
	<.,this,this/that.md,this/that.jpg,this/that.pdf> \
	[-|<object-name>] \
	[--count <2>]
 . md -> pdf.
@pdf \
	convert \
	[combine,~compress,filename=<release.pdf>,install,upload] \
	[.|<object-name>] \
	[--count <2>] \
	[--list_missing 0]
 . md -> pdf.
```
