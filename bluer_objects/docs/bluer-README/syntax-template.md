title:::

## ai

### ignore

ignore in the conversation with ai.

```python
ignore::: ai:::ignore

some text

ignore::: ai:::ignore
```

### objects

use `<object-name>` to store ai results.

```python
ignore::: ai:::object <object-name>
```

### prompt completion

complete `<prompt>`.

```python
ignore::: ai:::complete <unique-id> <prompt>
```

document the completed `<prompt>`.

```python
ignore::: ai:::completed <unique-id> <prompt>
```

## details

add details, such as this,

details:::example

this is an example.

details:::

```python
ignore::: details:::<summary>
ignore::: details:::
```

## environment variables

use the environment variable `ENV_NAME`.
```python
ignore::: env:::ENV_NAME
```

## help

show help about `<command>`.
```python
ignore::: help::: <command>
```

## images

clickable menu of images with descriptions.
```python
ignore::: items:::
```

## include a file

include `<filename>`.
```python
ignore::: include::: <filename>
ignore::: include:::noref <filename>
```

## links

to show images, or to make files downloadable.

link to `<filename>` in an `<object-name>` in an assets repo.
```python
ignore::: assets:::<object-name>/<filename>
ignore::: assets:::<volume>:::<object-name>/<filename>
```

downloadable link to `<object-name>`.
```python
ignore::: object:::<object-name>
ignore::: object:::<object-name>:::<filename>
```

## metadata

show metadata from `<object-name>`.
```python
ignore::: metadata:::<object-name>
ignore::: metadata:::<object-name>:::this.that
```

## objects

get `<object-name>` as set before (see ⬇️).
```python
ignore::: get:::<object_name>
```

set `<object-mame>` to use with get (see ⬆️).
```python
ignore::: set:::<object_name> <object-name>
ignore::: set:::<object_name> env:::ENV_NAME
ignore::: set:::<object_name> metadata:::<object-name>:::this.that
```

## signature

add signature.
```python
ignore::: signature:::
```

## title

add title.
```python
ignore::: title:::
ignore::: title:::<reference>
```