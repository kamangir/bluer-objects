# validation

## set & get

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
📂 object :: 2026-01-05-18-25-50-fcasoo
🌀  #️⃣  2026-01-05-18-25-50-fcasoo.tag-2026-01-05-rvf5um=value-2026-01-05-d8ktnu
🌀  S3Interface.download _serverless_objects/2026-01-05-18-25-50-fcasoo.yaml
✅ runme: value-2026-01-05-d8ktnu == value-2026-01-05-d8ktnu.
🌀  S3Interface.download _serverless_objects/2026-01-05-18-25-50-fcasoo.yaml
✅ runme:  is empty.
```

## search

```
runme() {
    local tag=tag-$(@@timestamp)
    local value

    ...

    @select
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
