# aliases: assets

asset management in [github/kamangir/assets](https://github.com/kamangir/assets), and its volumes: [2](https://github.com/kamangir/assets2).

```bash
@assets \
	cd \
	[create,vol=<3>] \
	[<path>]
 . cd assets volume.
@assets \
	mv \
	[~create,extension=<jpg>,vol=<3>] \
	[<this/that>] \
	[push,browse,~increment_version,offline,rpi=<machine-name>,scp,~status,test,]
 . mv assets to volume.
@assets \
	publish \
	[download,extensions=<png+txt>,~pull,push,vol=<3>] \
	[.|<object-name>] \
	[--asset_name <other-object-name>] \
	[--prefix <prefix>]
 . <object-name>/<prefix> -> assets.
```
