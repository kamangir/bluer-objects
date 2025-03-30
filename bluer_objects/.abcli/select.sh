#! /usr/bin/env bash

function abcli_select() {
    local object_name=$(abcli_clarify_object "$1" $(abcli_string_timestamp))

    local options=$2
    local do_open=$(abcli_option_int "$options" open 0)
    local type_name=$(abcli_option "$options" type object)

    local object_name_var_prev=abcli_${type_name}_name_prev
    export abcli_${type_name}_name_prev2=${!object_name_var_prev}

    local object_name_var=abcli_${type_name}_name
    export abcli_${type_name}_name_prev=${!object_name_var}

    export abcli_${type_name}_name=$object_name

    local object_path=$ABCLI_OBJECT_ROOT/$object_name
    export abcli_${type_name}_path=$object_path
    mkdir -p $object_path

    [[ "$type_name" == object ]] &&
        cd $object_path

    abcli_log "📂 $type_name :: $object_name"

    [[ "$do_open" == 1 ]] &&
        open $object_path

    return 0
}
