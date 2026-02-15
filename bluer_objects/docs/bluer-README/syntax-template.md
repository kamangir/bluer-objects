title:::

link to `<filename>` in an `<object-name>` in an assets repo.
```python
ignore::: assets:::<object-name>/<filename>
```

add details, such as this,

details:::example

this is an example.

details:::

```python
ignore::: details:::<summary>
ignore::: details:::
```

use the environment variable `ENV_NAME`.
```python
ignore::: env:::ENV_NAME
```

get `<object-name>` as set before (see ⬇️).
```python
ignore::: get:::<object_name>
```

show help about `<command>`.
```python
ignore::: help::: <command>
```

include `<filename>`.
```python
ignore::: include::: <filename>
ignore::: include:::noref <filename>
```

clickable menu of images with descriptions.
```python
ignore::: items:::
```

show metadata from `<object-name>`.
```python
ignore::: metadata:::<object-name>
ignore::: metadata:::<object-name>:::this.that
```

downloadable link to `<object-name>`.
```python
ignore::: object:::<object-name>
ignore::: object:::<object-name>:::<filename>
```

set `<object-mame>` to use with `get` (see ⬆️).
```python
ignore::: set:::<object_name> <object-name>
ignore::: set:::<object_name> env:::ENV_NAME
ignore::: set:::<object_name> metadata:::<object-name>:::this.that
```

add signature.
```python
ignore::: signature:::
```

add title.
```python
ignore::: title:::
ignore::: title:::<reference>
```