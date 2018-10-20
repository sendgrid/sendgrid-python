#!/usr/bin/env bash

# default arguments
host="https://github.com"
api_host="https://api.github.com"
origin="sendgrid"
repo="sendgrid-python"

# helpers
usage() {
  cat << EOF
Usage:
  generate_changelog [-h]
  generate_changelog [-v]

Options:
  -h        Print usage information
  -v        Specify the new version number
EOF
}

create_changelog() {

  content=""
  # Get merge commits
  merges="$(git log ${latest_release}..HEAD --merges --format="* %s (%h)" --grep="^Merge pull request #" | cut -d "#" -f2 | cut -d " " -f1)"
  for pr in $merges; do
    echo "Getting title of PR #$pr"
    url="$host/$origin/$repo/pull/$pr"
    api_url="$api_host/repos/$origin/$repo/pulls/$pr"
    title=$(curl -s $api_url | grep '"title": ' | cut -d '"' -f4)
    content="$content- [PR #$pr]($url): $title\n"
  done

  # Output changelog
  echo | awk -v v_header1="## [$version] - $(date +'%Y')-$(date +'%m')-$(date +'%d') ##" \
  -v v_header2="### Added" \
  -v v_content="$content" \
  '/All notable changes to this project will be documented in this file/{print;print v_header1;print v_header2;print v_content;next}1' CHANGELOG.md \
  > CHANGELOG.md.temp
  mv CHANGELOG.md.temp CHANGELOG.md
}


# script

# Exit if not in a Git repository.
if [ "true" != "$(git rev-parse --is-inside-work-tree 2> /dev/null)" ]
  then
    echo -e "This does not seem to be a Git repository.\n"
    exit
fi

# Parse all options
while [ "$1" != "" ]; do
    case $1 in
        -h | --help )           usage
                                exit
                                ;;
        -v | --version )        shift
                                version=$1
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
done

# Validate options
if [ "$version" == "" ]
  then
    echo "Must supply a version with -v"
    exit 1
fi

# Generate changelog from last tag
latest_release="$(git describe --tags --abbrev=0)"
create_changelog
echo "Successfully wrote to CHANGELOG.md"