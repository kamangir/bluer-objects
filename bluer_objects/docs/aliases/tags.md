# aliases: tags

```bash
@tags \
	clone \
	[..|<object-1>] \
	[.|<object-2>]
 . clone mlflow tags.
@tags \
	get \
	[.|<object-name>] \
	[--tag <tag>]
 . get mlflow tags|<tag> for <object-name>.
@tags \
	search \
	[<keyword-1>=<value-1>,<keyword-2>,~<keyword-3>] \
	[--count <-1>] \
	[--delim <space>] \
	[--log <0>] \
	[--offset <0>]
 . search mlflow.
@tags \
	set \
	[.|<object-name>] \
	[<keyword-1>=<value>,<keyword-2>,~<keyword-3>] \
	[--verbose 1]
 . set tags in mlflow.
```
