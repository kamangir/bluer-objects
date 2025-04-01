#! /usr/bin/env bash

function test_bluer_objects_clone() {
    local options=$1

    local source_object_name=test_bluer_objects_clone-$(abcli_string_timestamp_short)

    python3 -m bluer_objects.testing \
        create_test_asset \
        --object_name $source_object_name
    [[ $? -ne 0 ]] && return 1

    local object_name=test_bluer_objects_clone-$(abcli_string_timestamp_short)

    bluer_objects_clone \
        ~relate,~tags,~upload,$options \
        $source_object_name \
        $object_name
}
