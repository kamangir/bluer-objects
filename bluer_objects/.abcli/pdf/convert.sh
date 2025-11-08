#! /usr/bin/env bash

function bluer_objects_pdf_convert() {
    if [[ "$install" == 1 ]]; then
        pip install pypandoc
        brew install pandoc
    fi

    local module_name=${2:-bluer_ai}
    if alias "$module_name" &>/dev/null; then
        module_name=$(alias "$module_name" | sed -E "s/^alias $module_name='(.*)'$/\1/")
    fi

    local docs_path=$(python3 -m $module_name locate)/docs/

    local suffixes=${3:-.}

    local object_name=$(bluer_ai_clarify_object $4 pdf-$(bluer_ai_string_timestamp))

    bluer_ai_log "$module_name/$suffixes -> $object_name ..."

    bluer_ai_eval dryrun=$do_dryrun \
        python3 -m bluer_objects.pdf \
        convert \
        --docs_path $docs_path \
        --module_name $module_name \
        --object_name $object_name \
        --suffixes $suffixes \
        "${@:5}"
}
