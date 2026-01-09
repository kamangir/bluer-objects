#! /usr/bin/env bash

function bluer_objects_web_is_accessible() {
    local url=$1
    if [[ -z "$url" ]]; then
        bluer_ai_log_error "url not found."
        return 1
    fi

    python3 -m bluer_objects.web \
        is_accessible \
        --url $url
}

export BLUER_AI_IS_ONLINE=$(bluer_objects_web_is_accessible https://arvancloud.ir)
export INTERNET_IS_NATIONAL=$(bluer_ai_not $(bluer_objects_web_is_accessible https://github.com))

if [[ "$BLUER_AI_IS_ONLINE" == 1 ]]; then
    bluer_ai_log "🛜 online."

    [[ "$INTERNET_IS_NATIONAL" == 1 ]] &&
        bluer_ai_log "🇮🇷 internat is national."
else
    bluer_ai_log "⛓️‍💥 offline."
fi
