#! /usr/bin/env bash

function test_bluer_objects_pdf() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_objects_pdf \
        convert \
        bluer_objects \
        docs/templates \
        "${@:2}"

    return 0
}
