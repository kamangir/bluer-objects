# bluer-README: syntax

link to `<filename>` in an `<object-name>` in an assets repo.
```python
assets:::<object-name>/<filename>
```

add details, such as this,


<details>
<summary>example</summary>


this is an example.


</details>


```python
details:::<summary>
details:::
```

use the environment variable `ENV_NAME`.
```python
env:::ENV_NAME
```

get `<object-name>` as set before (see ⬇️).
```python
get:::<object_name>
```

show help about `<command>`.
```python
help::: <command>
```

include `<filename>`.
```python
include::: <filename>
include:::noref <filename>
```

clickable menu of images with descriptions.
```python
items:::
```

show metadata from `<object-name>`.
```python
metadata:::<object-name>
metadata:::<object-name>:::this.that
```

downloadable link to `<object-name>`.
```python
object:::<object-name>
object:::<object-name>:::<filename>
```

set `<object-mame>` to use with `get` (see ⬆️).
```python
set:::<object_name> <object-name>
set:::<object_name> env:::ENV_NAME
set:::<object_name> metadata:::<object-name>:::this.that
```

add signature.
```python
signature:::
```

add title.
```python
title:::
title:::<reference>
```
