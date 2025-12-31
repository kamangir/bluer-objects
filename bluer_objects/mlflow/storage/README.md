# validation

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