#! /usr/bin/env bash

function test_bluer_objects_pdf_convert_inline() {
    local options=$1

    local do_install=1
    [[ "$abcli_is_mac" == true ]] &&
        do_install=0

    local object_name=test_bluer_objects_pdf_convert-$(bluer_ai_string_timestamp)

    bluer_ai_eval ,$options \
        bluer_objects_pdf_convert \
        inline,install=$do_install,combine,$2 \
        bluer_objects \
        aliases,aliases/assets.md \
        $object_name \
        "${@:3}"

    return 0
}

function test_bluer_objects_pdf_convert() {
    local options=$1

    local object_name=test_bluer_objects_pdf_convert-2025-11-30-ci0cd7

    bluer_ai_eval ,$options \
        bluer_objects_pdf_convert \
        install=$do_install,combine,$2 \
        $object_name \
        "${@:3}"

    return 0
}
