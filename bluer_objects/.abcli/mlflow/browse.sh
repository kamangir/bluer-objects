#! /usr/bin/env bash

function bluer_objects_mlflow_browse() {
    local options=$1
    local browse_experiment=$(bluer_ai_option_int "$options" experiment 0)

    local url=$DATABRICKS_HOST/$ABCLI_MLFLOW_URL_SUBDOMAIN

    if [ $(bluer_ai_option_int "$options" databricks 0) == 1 ]; then
        url="https://accounts.cloud.databricks.com/"
    elif [ $(bluer_ai_option_int "$options" host 0) == 1 ]; then
        : # do nothing
    elif [ $(bluer_ai_option_int "$options" models 0) == 1 ]; then
        url="$url/models"
    else
        local object_name=$(bluer_ai_clarify_object $2 .)

        local experiment_id=$(bluer_objects_mlflow get_id $object_name)
        if [ -z "$experiment_id" ]; then
            bluer_ai_log_error "@mlflow: browse: $object_name: object not found."
            return 1
        fi
        bluer_ai_log "experiment id: $experiment_id"

        url="$url/experiments/$experiment_id"

        if [[ "$browse_experiment" == 0 ]]; then
            local last_run_id=$(bluer_objects_mlflow get_run_id $object_name --count 1)
            bluer_ai_log "last run id: $last_run_id"

            url="$url/runs/$last_run_id"
        fi
    fi

    bluer_ai_browse $url
}
