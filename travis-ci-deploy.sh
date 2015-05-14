#!/bin/bash
set -e
# make sure we are being called from the travis-ci environment
[[ $TRAVIS_BRANCH && $TRAVIS_PULL_REQUEST && ${GAE_CLIENT_ID} ]] || {
    echo "This script should be run in the travis-ci environment"
    exit
}

if [[ ${TRAVIS_PULL_REQUEST} == "false" ]]; then
    export GOOGLE_APPLICATION_CREDENTIALS=$TRAVIS_BUILD_DIR/buildconf/deploy/buildout-template-c3f13b4450c1.json
    wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip
    unzip -qq google-cloud-sdk.zip
    printf '\ny\n\ny\ny\n' | ./google-cloud-sdk/install.sh
    source google-cloud-sdk/path.bash.inc
    gcloud -q components update preview app
    gcloud -q auth activate-service-account ${GAE_CLIENT_ID} \
            --key-file buildconf/deploy/buildout-template-c3f13b4450c1.json
    gcloud -q --project buildout-template preview app deploy --version ${TRAVIS_BRANCH} --set-default app
fi
