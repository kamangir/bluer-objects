#! /usr/bin/env bash

export MLFLOW_TRACKING_URI="databricks"

function abcli_mlflow() {
    local task=$1

    local function_name=abcli_mlflow_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [[ ",get_id,get_run_id,rm," == *",$task,"* ]]; then
        local object_name=$(abcli_clarify_object $2 .)

        python3 -m bluer_objects.mlflow \
            $task \
            --object_name $object_name \
            "${@:3}"

        return
    fi

    abcli_log_error "@mlflow: $task: command not found."
    return 1
}

bluer_ai_source_caller_suffix_path /mlflow
