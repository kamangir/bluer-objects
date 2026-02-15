# bluer-README: syntax

## ai

### ignore

ignore in the conversation with ai.

```python
ai:::ignore

some text

ai:::ignore
```

### objects

use `<object-name>` to store ai results.

```python
ai:::object <object-name>
```

## details

add details, such as this,


<details>
<summary>example</summary>


this is an example.


</details>


```python
details:::<summary>
details:::
```

## environment variables

use the environment variable `ENV_NAME`.
```python
env:::ENV_NAME
```

## help

show help about `<command>`.
```python
help::: <command>
```

## images

clickable menu of images with descriptions.
```python
items:::
```

## include a file

include `<filename>`.
```python
include::: <filename>
include:::noref <filename>
```

## links

to show images, or to make files downloadable.

link to `<filename>` in an `<object-name>` in an assets repo.
```python
assets:::<object-name>/<filename>
```

downloadable link to `<object-name>`.
```python
object:::<object-name>
object:::<object-name>:::<filename>
```

## metadata

show metadata from `<object-name>`.
```python
metadata:::<object-name>
metadata:::<object-name>:::this.that
```

## objects

get `<object-name>` as set before (see ⬇️).
```python
get:::<object_name>
```

set `<object-mame>` to use with get (see ⬆️).
```python
set:::<object_name> <object-name>
set:::<object_name> env:::ENV_NAME
set:::<object_name> metadata:::<object-name>:::this.that
```

## signature

add signature.
```python
signature:::
```

## title

add title.
```python
title:::
title:::<reference>
```
