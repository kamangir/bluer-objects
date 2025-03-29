#! /usr/bin/env bash

function abcli_storage_download_file() {
    python3 -m bluer_objects.storage \
        download_file \
        --object_name "$1" \
        --filename "$2" \
        "${@:3}"
}
