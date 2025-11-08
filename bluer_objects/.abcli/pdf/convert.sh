#! /usr/bin/env bash

function bluer_objects_pdf_convert() {
    local module_name=${1:-bluer_ai}
    if alias "$module_name" &>/dev/null; then
        module_name=$(alias "$module_name" | sed -E "s/^alias $module_name='(.*)'$/\1/")
    fi

    local object_name=$(bluer_ai_clarify_object $2 pdf-$(bluer_ai_string_timestamp))

    local suffix=${3:-docs/README.md}

    bluer_ai_eval dryrun=$do_dryrun \
        python3 -m bluer_objects.pdf \
        convert \
        --module_name $module_name \
        --object_name $object_name \
        --suffix $suffix \
        "${@:3}"
}
