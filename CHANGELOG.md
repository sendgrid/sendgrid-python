# Change Log
All notable changes to this project will be documented in this file.

## [3.0.0] - XXXX-XX-XX
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
