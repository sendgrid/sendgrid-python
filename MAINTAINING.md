# Maintainers guide

This portion is here to document tasks specific to maintainers.

## Prerequisite

- We use [`bumpversion`](https://pypi.org/project/bumpversion/) to help with tagging and 
  updating the current version in all required places. You should have it installed, but 
  if not, you can get it with `pip install bumpversion`.
- Have access to the [sendgrid project on PyPI](https://pypi.org/project/sendgrid/).  

## Make a new release

You should be on the `master` branch, and up-to-date with the remote.

1. Make sure the `CHANGELOG.md` is up to date and has an entry for the new release with today's date. All files should be committed.
2. Update version digit and create git tag: `bumpversion [major|minor|patch]`.
3. Push changes with tags: `git push && git push --tags` 

Travis should take care of pushing to PyPI after the tests pass under Python 3.6.

## Travis deploy troubleshooting

Sometimes it fails, these should help.

### Invalid credentials

If Travis fails with a 403 error `Invalid or non-existent authentication information.`,
that your username or password are wrong. Check the username is spelled correctly 
and re-encrypt your password as described 
[in the Travis docs](https://docs.travis-ci.com/user/deployment/pypi/).

### Uploaded by multiple jobs

If the condition is wrong, Travis may try to upload to PyPI on more than 1 job,
which would result in error saying the distribution already exist. It's possible to
deploy on very specific [conditions](https://docs.travis-ci.com/user/deployment#conditional-releases-with-on).
