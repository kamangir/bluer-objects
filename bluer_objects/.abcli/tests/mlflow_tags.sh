#! /usr/bin/env bash

function test_bluer_objects_mlflow_tags_validation() {
    local object_name="test-object-$(bluer_ai_string_timestamp_short)"
    local tag="test-tag-$(bluer_ai_string_timestamp_short)"
    local value="test-value-$(bluer_ai_string_timestamp_short)"

    bluer_objects_mlflow tags set \
        $object_name \
        $tag=$value
    [[ $? -ne 0 ]] && return 1

    bluer_ai_assert \
        "$(bluer_objects_mlflow tags get $object_name --tag $tag)" \
        $value
    [[ $? -ne 0 ]] && return 1

    bluer_ai_assert \
        "$(bluer_objects_mlflow tags get $object_name --tag some-tag)" \
        - empty
}

function test_bluer_objects_mlflow_tags_search() {
    local options=$1

    bluer_objects_mlflow_tags search \
        this=that,what,~who \
        --log 0
    [[ $? -ne 0 ]] && return 1
}

function test_bluer_objects_mlflow_tags_search_serverless() {
    local MLFLOW_IS_SERVERLESS_=$MLFLOW_IS_SERVERLESS
    export MLFLOW_IS_SERVERLESS=1

    bluer_objects_mlflow_tags search \
        \"tags."this" = "that" and tags."what" = "True" and tags."who" = "False"\" \
        --server_style 1 \
        --log 0

    export MLFLOW_IS_SERVERLESS=MLFLOW_IS_SERVERLESS_
}
