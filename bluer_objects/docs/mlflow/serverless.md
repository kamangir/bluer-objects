# mlflow: serverless

validation.

# set & get

```bash
runme() {
    @select

    local tag=tag-$(@@timestamp)
    local value=value-$(@@timestamp)

    @mlflow tags set . \
            $tag=$value

    @assert \
        "$(@mlflow tags get . --tag $tag)" \
        $value
    [[ $? -ne 0 ]] && return 1

    @assert \
        "$(@mlflow tags get . --tag some-tag)" \
        - empty
}

runme
```

```text
📂 object :: 2026-01-06-14-22-38-42ei3i
🌀  #️⃣  2026-01-06-14-22-38-42ei3i.tag-2026-01-06-q60ucb=value-2026-01-06-i9kbzz
✅ runme: value-2026-01-06-i9kbzz == value-2026-01-06-i9kbzz.
✅ runme:  is empty.
```

# search

```bash
runme() {
    local tag=tag-$(@@timestamp)
    local value=value-$(@@timestamp)

    local object_name=test-$(@@timestamp)

    @mlflow tags set \
        $object_name \
        $tag=$value

    @assert \
        $(@mlflow tags search $tag=$value \
        --log 0) \
        $object_name
}

runme
```

```text
🌀  #️⃣  test-2026-01-06-62gv6y.tag-2026-01-06-ciltlx=value-2026-01-06-sksthl
✅ runme: test-2026-01-06-62gv6y == test-2026-01-06-62gv6y.
```
