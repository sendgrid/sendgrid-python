# Change Log
All notable changes to this project will be documented in this file.

## [3.6.5] - 2017-03-30 ##
### Updated
- Pull #300 [Exclude test package](https://github.com/sendgrid/sendgrid-python/pull/250)
- Big thanks to [Iryna Shcherbina](https://github.com/irushchyshyn) for the pull request!

## [3.6.4] - 2017-03-29 ##
### Updated
- Pull #250 [Improve code quality](https://github.com/sendgrid/sendgrid-python/pull/250)
- Big thanks to [Andrii Soldatenko](https://github.com/andriisoldatenko) for the pull request!

## [3.6.3] - 2016-11-10 ##
### Updated
- Pull #243 [Update deprecated Heroku command](https://github.com/sendgrid/sendgrid-python/pull/243)
- Big thanks to [Roberto Ortega](https://github.com/berto) for the pull request!

## [3.6.2] - 2016-11-10 ##
### Fixed
- Pull #240 [Add six to requirements.txt](https://github.com/sendgrid/sendgrid-python/pull/246)
- Big thanks to [Wataru Sato](https://github.com/awwa) for the pull request!

## [3.6.1] - 2016-11-10 ##
### Fixed
- Pull #246 [Typo 'user' for 'usr'](https://github.com/sendgrid/sendgrid-python/pull/246)
- Big thanks to [Mike Ralphson](https://github.com/MikeRalphson) for the pull request!

## [3.6.0] - 2016-10-11 ##
### Added
- Pull #234 [Substitutions allow non-strings for values](https://github.com/sendgrid/sendgrid-python/pull/234)
- Big thanks to [ittus](https://github.com/ittus) for the pull request!

## [3.5.0] - 2016-10-11 ##
### Added
- Pull #233: [Allow dict to be passed to add_headers](https://github.com/sendgrid/sendgrid-python/pull/233)
- Big thanks to [Navin Pai](https://github.com/navinpai) for the pull request!

## [3.4.0] - 2016-09-02 ##
### Added
- Pull #215
- Support larger files. Note that there is a 20MB maximum.

## [3.3.1] - 2016-08-31 ##
### Fixed
- Pull #213
- Naming inconsistency, we now standardized on `file_name`
- Support for use of `iteritems` in Python 3

## [3.3.0] - 2016-08-31 ##
### Updated
- Pull #212
- Allow for custom Inbound Parse config.yml

## [3.2.3] - 2016-08-31 ##
### Updated
- Pull #211
- Within sendgrid/helpers/inbound/parse.py - moved doc strings to be under function definitions
- broke up def attachments(...) into two individual private functions, so it's a bit less cumbersome and can be individually tested better
- Big thanks to [Christopher Li](https://github.com/LiYChristopher) for the pull request!

## [3.2.2] - 2016-08-23 ##
### Added
- Table of Contents in the README
- Added a [USE_CASES.md](https://github.com/sendgrid/sendgrid-python/blob/master/USE_CASES.md) section, with the first use case example for transactional templates

## [3.2.1] - 2016-08-17 ##
### Fixed
- pep8 formatting
- include Heroku config files in PyPi

## [3.2.0] - 2016-08-17 ##
### Added
- Helper code for our [Inbound Parse webhook](https://github.com/sendgrid/sendgrid-python/tree/inbound/sendgrid/helpers/inbound)

## [3.1.10] - 2016-07-26 ##
### Fixed
- Release 3.1.9 was botched (sorry!), so [the apikey/api_key fix](https://github.com/sendgrid/sendgrid-python/issues/197) 3.1.9 was supposed to address is now in this release

## [3.1.9] - 2016-07-26 ##
### Fixed
- [Issue #197](https://github.com/sendgrid/sendgrid-python/issues/197): api_key / apikey attribute logic incorrect
- Thanks to [johguse](https://github.com/johguse) for reporting the bug

## [3.1.8] - 2016-07-25 ##
### Added
- [Troubleshooting](https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md) section

## [3.1.7] - 2016-07-25 ##
### Added
- Solves [issue 195](https://github.com/sendgrid/sendgrid-python/pull/195)
- The variable apikey and api_key are now interchangeable to help support those migrating from v2
- Thanks to [Ian Douglas](https://github.com/iandouglas) for the feedback!

## [3.0.7] - 2016-07-20 ##
### Added
- README updates
- Update introduction blurb to include information regarding our forward path
- Update the v3 /mail/send example to include non-helper usage
- Update the generic v3 example to include non-fluent interface usage

## [3.0.6] - 2016-07-12 ##
### Added
- Update docs, unit tests and examples to include Sender ID

## [3.0.5] - 2016-07-11 ##
### Fixed
- Fixed logic errors related to issue #189

## [3.0.4] - 2016-07-08 ##
### Fixed
- Dependency update to fix issue #186

## [3.0.3] - 2016-07-07 ##
### Added
- Tests now mocked automatically against [prism](https://stoplight.io/prism/)

## [3.0.1] - 2016-07-05 ##
### Fixed
- [Issue 185](https://github.com/sendgrid/sendgrid-python/issues/185): Getting HTTP Error 406 when getting bounces
### Updated
- Examples, USAGE.md and Unit Tests with updated content and new endpoints

## [3.0.0] - 2016-06-13 ##
### Added
- Breaking change to support the v3 Web API
- New HTTP client
- v3 Mail Send helper

## [2.1.1] - 2016-03-02 ##

### Added ###

- you can now pass a path to your .env file to the SendGridAPIClient

## [2.1.1] - 2016-03-02 ##

### Added ###

- you can now pass an apikey to the SendGridAPIClient, per issue [#168](https://github.com/sendgrid/sendgrid-python/issues/168). Thanks [Matt](https://github.com/mbernier)!
- fix .rst formatting for PyPi

## [2.0.0] - 2016-03-01 ##

### Added ###

- breaking change is only for the Web API v3 endpoints
- we now have support for all Web API v3 endpoints

## [1.6.22] - 2015-02-08 ##

### Fixed ###

- a call to GET api_keys after a call to DELETE api_keys would throw an error.

## [1.6.21] - 2015-02-08 ##

### Added ###

- the timeout value is no longer hard coded.

## [1.6.20] - 2015-02-04 ##

### Updated ###

- smtpi-sendgrid dependency is now 0.3.1, the latest version: [161](https://github.com/sendgrid/sendgrid-python/pull/161/files). Thanks [Kevin Brown](https://github.com/kevin-brown)!

## [1.5.20] - 2015-01-12 ##

### Added ###

- Change timeout to opts variable [157](https://github.com/sendgrid/sendgrid-python/pull/157)
- Thanks [tgehrs](https://github.com/tgehrs)!

## [1.5.19] - 2015-12-03 ##

### Fixed ###

- Can't install normally [155](https://github.com/sendgrid/sendgrid-python/issues/155)

## [1.5.18] - 2015-11-17 ##

### Fixed ###

- Fix "HTTP 406 Not Acceptable Errors" [149](https://github.com/sendgrid/sendgrid-python/issues/149)

## [1.5.17] - 2015-11-17 ##

### Added ###

- Global Stats [GET]

## [1.5.16] - 2015-11-17 ##

### Added ###

- Template Engine documentation
- SMTPAPI documentation

## [1.5.15] - 2015-11-17 ##

### Added ###

- API Keys documentation for [POST, PATCH, DELETE]

## [1.5.14] - 2015-11-09 ##

### Fixed ###
- Fix "Mail uses old-style class again" [144](https://github.com/sendgrid/sendgrid-python/issues/144)

## [1.5.13] - 2015-10-28 ##

### Fixed ###
- Fix timeout via URLError [104](https://github.com/sendgrid/sendgrid-python/issues/104)

## [1.5.12] - 2015-10-28 ##

### Fixed ###
- Minor Refactor and README update

## [1.5.11] - 2015-10-27 ##

### Fixed ###
- ASM Global Suppressions [POST]

## [1.5.10] - 2015-10-26 ##

### Added ###
- ASM Global Suppressions [DELETE]

## [1.5.9] - 2015-10-26 ##

### Added ###
- Supression Unsubscribes [GET]

## [1.5.8] - 2015-10-21 ##

### Added ###
- Global Suppressions [GET]

## [1.5.7] - 2015-10-19 ##


### Added ###
- Include MIT.LICENSE in release tarball

## [1.5.6] - 2015-10-16 ##

### Fixed ###
- Removed unsupported endpoint

## [1.5.5] - 2015-10-16 ##

### Added ###
- Added Unsubscribe Groups [POST]

## [1.5.4] - 2015-10-15 ##

### Added ###
- Global Suppressions [GET]

## [1.5.3] - 2015-09-29 ##

### Added ###
- Refactored tests and added Tox support
- Framework for Web API v3 endpoints
- Web API v3 endpionts: apikeys, ASM groups and ASM suppressions

### Fixed  ###
- Python 3 Fix [#126](https://github.com/sendgrid/sendgrid-python/issues/126)

## [1.4.3] - 2015-09-22 ##

### Fixed ###
- Reply To header now supports friendly name [#110](https://github.com/sendgrid/sendgrid-python/issues/110)

## [1.4.2] - 2015-09-15 ##

### Added ###
- Upgrade Mail to new-style class, on Python 2.x.

## [1.4.1] - 2015-09-09 ##

### Added ###
- Classifiers for compatible python versions

## [1.4.0] - 2015-04-27 ##

### Added ###
- Support for API keys

## [1.3.0] - 2015-01-23 ##

### Added ###
- Add new method for ASM Group ID via [#98](https://github.com/sendgrid/sendgrid-python/pull/98)
- Add CHANGELOG.md
