#! /usr/bin/env bash

function bluer_objects_pdf_convert() {
    local options=$1
    local do_install=$(bluer_ai_option_int "$options" install 0)
    local do_combine=$(bluer_ai_option_int "$options" combine 0)
    local do_compress=$(bluer_ai_option_int "$options" compress $do_combine)
    local load_yaml=$(bluer_ai_option_int "$options" yaml 0)

    if [[ "$do_install" == 1 ]]; then
        pip install pypandoc
        pip install PyPDF2

        if [[ "$abcli_is_mac" == true ]]; then
            brew install pandoc
            brew install wkhtmltopdf
            brew install ghostscript
        fi
    fi

    if [[ "$load_yaml" == 1 ]]; then
        local filename=$(bluer_ai_option "$options" filename release.yaml)

        local object_name=$(bluer_ai_clarify_object $2 .)

        bluer_ai_log "@pdf $object_name/$filename ..."

        bluer_ai_eval dryrun=$do_dryrun \
            python3 -m bluer_objects.pdf \
            convert \
            --filename $filename \
            --load_yaml $load_yaml \
            --object_name $object_name \
            --combine $do_combine \
            "${@:5}"
        [[ $? -ne 0 ]] && return 1
    else
        local module_name=${2:-bluer_ai}

        if alias "$module_name" &>/dev/null; then
            module_name=$(alias "$module_name" | sed -E "s/^alias $module_name='(.*)'$/\1/")
        fi

        local docs_path=$(python3 -m $module_name locate)/docs/

        local suffixes=${3:-.}

        local object_name=$(bluer_ai_clarify_object $4 pdf-$(bluer_ai_string_timestamp))

        bluer_ai_log "@pdf $module_name/$suffixes -> $object_name ..."

        bluer_ai_eval dryrun=$do_dryrun \
            python3 -m bluer_objects.pdf \
            convert \
            --docs_path $docs_path \
            --module_name $module_name \
            --object_name $object_name \
            --suffixes $suffixes \
            --combine $do_combine \
            "${@:5}"
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ "$do_compress" == 1 ]]; then
        bluer_ai_log "compressing..."

        local object_path=$ABCLI_OBJECT_ROOT/$object_name
        mv -v \
            $object_path/release.pdf \
            $object_path/_release.pdf

        gs -sDEVICE=pdfwrite \
            -dCompatibilityLevel=1.4 \
            -dPDFSETTINGS=/ebook \
            -dNOPAUSE \
            -dBATCH \
            -sOutputFile=$object_path/release.pdf \
            $object_path/_release.pdf
        [[ $? -ne 0 ]] && return 1

        rm $object_path/_release.pdf
        bluer_ai_log "-> $object_path/release.pdf"
    fi
}
