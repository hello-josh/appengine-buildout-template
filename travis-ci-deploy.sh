#!/bin/bash
set -e
# make sure we are being called from the travis-ci environment
[[ $TRAVIS_BRANCH && $TRAVIS_PULL_REQUEST && ${GAE_CLIENT_ID} ]] || {
    echo "This script should be run in the travis-ci environment"
    exit
}

if [[ ${TRAVIS_PULL_REQUEST} == "false" ]]; then
    wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip
    unzip -qq google-cloud-sdk.zip
    google-cloud-sdk/install.sh --usage-reporting false \
                                --path-update false \
                                --rc-path=~/.bashrc \
                                --bash-completion false \
                                --override-components=app
    source google-cloud-sdk/path.bash.inc
    gcloud components update preview app
    gcloud auth activate-service-account ${GAE_CLIENT_ID} \
            --key-file buildconf/deploy/buildout-template-c3f13b4450c1.json
    gcloud --project buildout-template preview app deploy --version ${TRAVIS_BRANCH} app
fi
