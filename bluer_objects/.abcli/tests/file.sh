#! /usr/bin/env bash

function test_file_asset() {
    echo $abcli_path_git/bluer-objects/bluer_objects/.abcli/tests/file.sh
}

function test_file_replace() {
    local options=$1

    local filename=$abcli_path_git/file.sh

    cp -v \
        $(test_file_asset) \
        $filename

    bluer_ai_eval ,$options \
        bluer_objects_file replace \
        $filename \
        --this function+local \
        --that FUNCTION+LOCAL \
        "${@:2}"

    bluer_ai_cat $filename
}

function test_file_size() {
    local options=$1

    # ---

    local size=$(bluer_objects_file size \
        $(test_file_asset))

    bluer_ai_assert \
        "$size" \
        "0.85 kB"
    [[ $? -ne 0 ]] && return 1

    # ---

    local size=$(bluer_objects_file size \
        $(test_file_asset) \
        --pretty 0)

    bluer_ai_assert \
        "$size" \
        "867"
}
