#! /usr/bin/env bash

function bashtest() {
    # set -x # verbose-mode

    local plugin_name=$1

    cd ..
    git clone https://github.com/kamangir/blue-ai.git

    source $(pwd)/blue-ai/blue_ai/.abcli/blue_ai.sh ~terraform \
        $plugin_name test

    return
}

bashtest "$@"
