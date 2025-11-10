#! /usr/bin/env bash

function test_bluer_objects_pdf_convert() {
    local options=$1

    local object_name=test_bluer_objects_pdf_convert-$(bluer_ai_string_timestamp)

    bluer_ai_eval ,$options \
        bluer_objects_pdf_convert \
        install,combine,$options \
        bluer_objects \
        aliases,aliases/assets.md \
        $object_name \
        "${@:2}"

    # TODO: validate that release.pdf exists
}

function test_bluer_objects_pdf_convert_yaml() {
    local options=$1

    local object_name=test_bluer_objects_pdf_convert_yaml-$(bluer_ai_string_timestamp)

    # TODO: create release.yaml

    bluer_ai_eval ,$options \
        bluer_objects_pdf_convert \
        install,combine,yaml,$options \
        $object_name \
        "${@:2}"

    # TODO: validate that release.pdf exists
}
