# aliases: metadata

```bash
@metadata \
	get \
	[delim=+,dict.keys,dict.values,filename,key=<key>] \
	<filename.yaml>
 . get <filename.yaml>[<key>]
@metadata \
	get \
	[delim=+,dict.keys,dict.values,filename=<metadata.yaml>,key=<key>,object] \
	[.|<object-name>]
 . get <object-name>/metadata[<key>]
@metadata \
	get \
	[delim=+,dict.keys,dict.values,filename=<metadata.yaml>,key=<key>,path] \
	<path>
 . get <path>/metadata[<key>]
@metadata \
	post \
	<key> \
	<value> \
	filename \
	<filename.yaml> \
	[--verbose 1]
 . <filename.yaml>[<key>] = <value>
@metadata \
	post \
	<key> \
	<value> \
	object,filename=<metadata.yaml> \
	[.|<object-name>] \
	[--verbose 1]
 . <object-name>[<key>] = <value>
@metadata \
	post \
	<key> \
	<value> \
	path,filename=<metadata.yaml> \
	<path> \
	[--verbose 1]
 . <path>[<key>] = <value>
```
