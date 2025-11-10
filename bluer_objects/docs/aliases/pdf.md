# aliases: pdf

```bash
@pdf \
	convert \
	[install,combine,~compress] \
	<module-name> \
	<.,this,this/that.md,this/that.jpg,this/that.pdf> \
	[-|<object-name>]
 . md -> pdf.
@pdf \
	convert \
	[filename=<filename.yaml>,install,combine,~compress,yaml] \
	[.|<object-name>]
 . md -> pdf.
```
