#! /usr/bin/env bash

abcli_source_caller_suffix_path /tests

abcli_env_dot_load \
    caller,plugin=bluer_objects,suffix=/../..

abcli_env_dot_load \
    caller,filename=config.env,suffix=/..
