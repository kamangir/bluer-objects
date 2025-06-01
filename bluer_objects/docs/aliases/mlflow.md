# mlflow

```bash
@mlflow \
	browse \
	[experiment,models] \
	[.|<object-name>]
 . browse mlflow.
@mlflow \
	cache \
	read \
	<keyword>
 . read mlflow.cache[<keyword>].
@mlflow \
	cache \
	write \
	<keyword> \
	<value>
 . write mlflow.cache[<keyword>]=value.
@mlflow \
	deploy \
	[dryrun,~local,port=<5001>]
 . deploy mlflow.
@mlflow \
	get_id \
	[.|<object-name>]
 . get mlflow id for <object-name>.
@mlflow \
	get_run_id \
	[.|<object-name>] \
	[--count <1>] \
	[--delim <space>] \
	[--offset <0>]
 . get mlflow run ids for <object-name>.
@mlflow \
	list_registered_models
 . list mlflow registered models.
@lock \
	lock \
	[.|<object-name>] \
	[--lock <lock-name>] \
	[--timeout <10>] \
	[--verbose 0]
 . lock <object-name>.
@lock \
	unlock \
	[.|<object-name>] \
	[--lock <lock-name>] \
	[--verbose 0]
 . unlock <object-name>.
@mlflow \
	log_artifacts \
	[.|<object-name>] \
	[--model_name <model-name>]
 . <object-name> -artifacts-> mlflow.
@mlflow \
	log_run \
	[.|<object-name>]
 . <object-name> -run-> mlflow.
@mlflow \
	rm \
	[.|<object-name>]
 . rm <object-name> from mlflow.
@mlflow \
	run \
	start | end \
	[.|<object-name>]
 . start | end mlflow run.
@mlflow \
	tags \
	clone \
	[..|<object-1>] \
	[.|<object-2>]
 . clone mlflow tags.
@mlflow \
	tags \
	get \
	[.|<object-name>] \
	[--tag <tag>]
 . get mlflow tags|<tag> for <object-name>.
@mlflow \
	tags \
	search \
	[explicit] \
	[--count <-1>] \
	[--delim <space>] \
	[--log <0>] \
	[--offset <0>] \
	[--filter_string <filter-string>]
 . search mlflow for <filter-string>
   <finter-string>: https://www.mlflow.org/docs/latest/search-experiments.html
@mlflow \
	tags \
	search \
	[<keyword-1>=<value-1>,<keyword-2>,~<keyword-3>] \
	[--count <-1>] \
	[--delim <space>] \
	[--log <0>] \
	[--offset <0>]
 . search mlflow.
@mlflow \
	tags \
	set \
	[.|<object-name>] \
	[<keyword-1>=<value>,<keyword-2>,~<keyword-3>]
 . set tags in mlflow.
@mlflow \
	test \
	[dryrun]
 . test mlflow.
@mlflow \
	transition \
	[model=<model-name>,stage=<stage>,version=<version>] \
	[<description>]
 . transition <model-name>.
   stage: Staging | Production | Archived
```
