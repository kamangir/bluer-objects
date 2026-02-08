# aliases: assets

asset management in [github/kamangir/assets](https://github.com/kamangir/assets), and its volumes: [2](https://github.com/kamangir/assets2).

```bash
@assets \
	cd \
	[create,vol=<2>] \
	[<path>]
 . cd assets volume.
@assets \
	mv \
	[~create,extension=<jpg>,vol=<2>] \
	[<this/that>] \
	[push,browse,~increment_version,offline,rpi=<machine-name>,scp,~status,test,]
 . mv assets to volume.
@assets \
	publish \
	[download,extensions=<png+txt>,~pull,push] \
	[.|<object-name>] \
	[--asset_name <other-object-name>] \
	[--prefix <prefix>]
 . <object-name>/<prefix> -> assets.
```
