# Change Log
All notable changes to this project will be documented in this file.

## [6.0.0] - TBD

- https://github.com/sendgrid/sendgrid-python/pull/486
- https://github.com/sendgrid/sendgrid-python/pull/488
- https://github.com/sendgrid/sendgrid-python/pull/493 
- https://github.com/sendgrid/sendgrid-python/pull/496
- https://github.com/sendgrid/sendgrid-python/pull/509 
- https://github.com/sendgrid/sendgrid-python/pull/510
- https://github.com/sendgrid/sendgrid-python/pull/512
- https://github.com/sendgrid/sendgrid-python/pull/524

## [5.4.1] - 2018-06-26 ##
### Fixed
- [PR #585](https://github.com/sendgrid/sendgrid-python/pull/585): Fix typo in `mail_example.py`. Big thanks to [Anurag Anand](https://github.com/theanuraganand) for the PR!
- [PR #583](https://github.com/sendgrid/sendgrid-python/pull/585): Fix `Personalization.substitutions` setter. Trying to set substitutions directly rather than with add_substitution was causing an infinite regress. Big thanks to [Richard Nias](https://github.com/richardnias) for the PR!

## [5.4.0] - 2018-06-07 ##
### Added
- [PR #384](https://github.com/sendgrid/sendgrid-python/pull/384): Adds how to set up domain whitelabel and how to view email statistics. Big thanks to [Aditya Tandon](https://github.com/adityatandon007) for the PR!
- [PR #427](https://github.com/sendgrid/sendgrid-python/pull/427): Increase config.py coverage. Big thanks to [Jeferson Daniel](https://github.com/jefersondaniel) for the PR!
- [PR #423](https://github.com/sendgrid/sendgrid-python/pull/423): Update config.py with better file handling. Big thanks to [Ajitesh Rai](https://github.com/ajiteshr7) for the PR!
- [PR #449](https://github.com/sendgrid/sendgrid-python/pull/449): Add a .env_sample file and Update README.md. Big thanks to [trangttt](https://github.com/trangttt) for the PR!
- [PR #463](https://github.com/sendgrid/sendgrid-python/pull/449): Add code climate.
- [PR #455](https://github.com/sendgrid/sendgrid-python/pull/455): Use with context manager and a few PEP8 changes. Big thanks to [Tim](https://github.com/The-White-Wolf) for the PR!
- [PR #470](https://github.com/sendgrid/sendgrid-python/pull/470): Modularize lengthy method. Big thanks to [Suprith Kumar Suvarneshwar](https://github.com/suprithIUB) for the PR!
- [PR #425](https://github.com/sendgrid/sendgrid-python/pull/425): Add tests for sendgrid.py apikey and api_key setters. Big thanks to [Krista LaFentres](https://github.com/lafentres) for the PR!
- [PR #446](https://github.com/sendgrid/sendgrid-python/pull/446): Added PULL_REQUEST_TEMPLATE. Big thanks to [Aleksandr Sobolev](https://github.com/s0b0lev) for the PR!
- [PR #472](https://github.com/sendgrid/sendgrid-python/pull/472): Moved mail helper classes into separate files. Big thanks to [Milos Pejanovic](https://github.com/runz0rd) for the PR!
- [PR #481](https://github.com/sendgrid/sendgrid-python/pull/481): Documented the new error handling functionality from python-http-client. Big thanks to [Manjiri Tapaswi](https://github.com/mptap) for the PR!
- [PR #418](https://github.com/sendgrid/sendgrid-python/pull/418): Add test for apps.py. Big thanks to [Sinan Comert](https://github.com/scomert) for the PR!
- [PR #438](https://github.com/sendgrid/sendgrid-python/pull/438): Update docstrings/pydoc/help. Big thanks to [Gabriel Krell](https://github.com/gabrielkrell) for the PR!
- [PR #413](https://github.com/sendgrid/sendgrid-python/pull/413): Error-checking in Mail helper/ASM. Big thanks to [Gabriel Krell](https://github.com/gabrielkrell) for the PR!
- [PR #518](https://github.com/sendgrid/sendgrid-python/pull/518): Announcement about Data Platform Engineer posting. Big thanks to [Marghodk](https://github.com/Marghodk) for the PR!
- [PR #479](https://github.com/sendgrid/sendgrid-python/pull/479): Add Project tests. Big thanks to [Peter Hampton](https://github.com/pjhampton) for the PR!
- [PR #480](https://github.com/sendgrid/sendgrid-python/pull/480): Test to check year in LICENSE.txt. Big thanks to [Navin Pai](https://github.com/navinpai) for the PR!
- [PR #476](https://github.com/sendgrid/sendgrid-python/pull/476): Add tests for Send.py. Big thanks to [Artiem K.](https://github.com/artiemq) for the PR!
- [PR #366](https://github.com/sendgrid/sendgrid-python/pull/366): Add AWS app tutorial to USE_CASES.md. Big thanks to [Mike Vanbuskirk](https://github.com/codevbus) for the PR!
- [PR #365](https://github.com/sendgrid/sendgrid-python/pull/365): Write tutorial to deploy simple Django app on Heroku. Big thanks to [Kan Ouivirach](https://github.com/zkan) for the PR!
- [PR #526](https://github.com/sendgrid/sendgrid-python/pull/526): Include code reviews section. Big thanks to [Jared Scott](https://github.com/jlax47) for the PR!
- [PR #414](https://github.com/sendgrid/sendgrid-python/pull/414): Provide utf-8 as encoding explicitly when opening text files. Big thanks to [Ruslan Shestopalyuk](https://github.com/rshest) for the PR!
- [PR #537](https://github.com/sendgrid/sendgrid-python/pull/537): Add unittesting support to .codeclimate.yml. Big thanks to [Prashu Chaudhary](https://github.com/prashuchaudhary) for the PR!
- [PR #554](https://github.com/sendgrid/sendgrid-python/pull/554): Ensure params are applied independently. Big thanks to [Nino Milenovic](https://github.com/rubyengineer) for the PR!
- [PR #557](https://github.com/sendgrid/sendgrid-python/pull/557): Client cleanup. Big thanks to [Slam](https://github.com/3lnc) for the PR!
- [PR #569](https://github.com/sendgrid/sendgrid-python/pull/569): Make Mail helper parameters truly optional. Big thanks to [Ian Beck](https://github.com/onecrayon) for the PR!

### Fixed
- [PR #415](https://github.com/sendgrid/sendgrid-python/pull/415): Typos. Big thanks to [Mohd Huzaifa Faruqui](https://github.com/huzaifafaruqui) for the PR!
- [PR #421](https://github.com/sendgrid/sendgrid-python/pull/421): Typos. Big thanks to [Abhishek Bhatt](https://github.com/ab-bh) for the PR!
- [PR #432](https://github.com/sendgrid/sendgrid-python/pull/432): Typos. Big thanks to [Gaurav Arora](https://github.com/gaurav61) for the PR!
- [PR #431](https://github.com/sendgrid/sendgrid-python/pull/431): Typos. Big thanks to [Gaurav Arora](https://github.com/gaurav61) for the PR!
- [PR #430](https://github.com/sendgrid/sendgrid-python/pull/430): Attempt to sync before executing shell command. Big thanks to [Aditya Narayan](https://github.com/aditnryn) for the PR!
- [PR #429](https://github.com/sendgrid/sendgrid-python/pull/429): Typos. Big thanks to [daluntw](https://github.com/daluntw) for the PR!
- [PR #492](https://github.com/sendgrid/sendgrid-python/pull/492): 
Updated date-range in LICENSE file. Big thanks to [Dhruv Srivastava](https://github.com/dhruvhacks) for the PR!
- [PR #482](https://github.com/sendgrid/sendgrid-python/pull/482): Typos. Big thanks to [Karan Samani](https://github.com/Kimi450) for the PR!
- [PR #504](https://github.com/sendgrid/sendgrid-python/pull/504): Fix .codeclimate.yml. Big thanks to [Matt Bernier](https://github.com/mbernier) for the PR!
- [PR #505](https://github.com/sendgrid/sendgrid-python/pull/505): Remove unnecessary github PR templates. Big thanks to [Alex](https://github.com/pushkyn) for the PR!
- [PR #494](https://github.com/sendgrid/sendgrid-python/pull/494): Remove unused import in register.py. Big thanks to [Alexis Rivera De La Torre](https://github.com/gardlt) for the PR!
- [PR #469](https://github.com/sendgrid/sendgrid-python/pull/469): 
Removed the trailing white spaces. Big thanks to [Siddaram Halli](https://github.com/SidduH) for the PR!
- [PR #484](https://github.com/sendgrid/sendgrid-python/pull/484): Python style fixes. Big thanks to [Gabriel Krell](https://github.com/gabrielkrell) for the PR!
- [PR #508](https://github.com/sendgrid/sendgrid-python/pull/508): Typos. Big thanks to [Saksham Gupta](https://github.com/shucon) for the PR!
- [PR #353](https://github.com/sendgrid/sendgrid-python/pull/353): Typos. Big thanks to [Yothin M](https://github.com/yothinix) for the PR!
- [PR #564](https://github.com/sendgrid/sendgrid-python/pull/564): Typos. Big thanks to [Chao](https://github.com/chaoranxie) for the PR!
- [PR #424](https://github.com/sendgrid/sendgrid-python/pull/424): Updating version 2.7.8 to 2.7.11 to match version in pyenv install instruction. Big thanks to [Krista LaFentres](https://github.com/lafentres) for the PR!
- [PR #454](https://github.com/sendgrid/sendgrid-python/pull/454): Requests to send mail with both plain text and HTML content fail if the HTML content is specified first. Big thanks to [Ryan D'souza](https://github.com/dsouzarc) for the PR!
- [PR #466](https://github.com/sendgrid/sendgrid-python/pull/466): Fixed PEP8 issues. Big thanks to [Piotr Szwarc](https://github.com/blackpioter) for the PR!
- [PR #522](https://github.com/sendgrid/sendgrid-python/pull/522): Typos. Big thanks to [Abhishek J](https://github.com/slashstar) for the PR!
- [PR #514](https://github.com/sendgrid/sendgrid-python/pull/514): Fix method_complexity issue in sendgrid/helpers/mail/ganalytics.py. Big thanks to [Chetan Kumar](https://github.com/chetankm-cs) for the PR!
- [PR #515](https://github.com/sendgrid/sendgrid-python/pull/515): Typos. Big thanks to [Mohd Ali Rizwi](https://github.com/alirizwi) for the PR!
- [PR #519](https://github.com/sendgrid/sendgrid-python/pull/519): Typos. Big thanks to [Aashish Gaba](https://github.com/ishucr7) for the PR!
- [PR #532](https://github.com/sendgrid/sendgrid-python/pull/532): Typos. Big thanks to [~](https://github.com/delirious-lettuce) for the PR!
- [PR #533](https://github.com/sendgrid/sendgrid-python/pull/533): Fix shadowed builtins, `id` -> `id_`. Big thanks to [~](https://github.com/delirious-lettuce) for the PR!
- [PR #581](https://github.com/sendgrid/sendgrid-python/pull/581): Typos. Big thanks to [Silvia Botros](https://github.com/silviabotros) for the PR!
- [PR #513](https://github.com/sendgrid/sendgrid-python/pull/513): Typos. Big thanks to [thepriefy](https://github.com/thepriefy) for the PR!
- [PR #538](https://github.com/sendgrid/sendgrid-python/pull/538): Fix bug in get_mock_personalization_dict(). Big thanks to [PierreMonico](https://github.com/PierreMonico) for the PR!
- [PR #543](https://github.com/sendgrid/sendgrid-python/pull/543): Typos. Big thanks to [Matthieu Bonnefoy](https://github.com/mbonnefoy) for the PR!

## [5.3.0] - 2017-10-23 ##
### Added
- Pull #348: Allows users to submit rfc822 formatted email addresses
- Big thanks to [Matt Bernier](https://github.com/mbernier) for the pull request!

## [5.2.1] - 2017-10-21 ##
### Fixed
- Pull #364: Install prism with non superuser account 
- Big thanks to [meahow](https://github.com/meahow) for the pull request!

## [5.2.0] - 2017-08-31 ##
### Added
- Pull #335: Permit unicode string values with Substitution helper
- Big thanks to [Mehron Kugler](https://github.com/mehronkugler) for the pull request!

## [5.1.0] - 2017-08-30 ##
### Added
- Pull #338: Allow the `__str__` method for the `Mail` object return an `String` instead of a `NoneType`
- Solves #292: The `__str__` method of the `Mail` class, doesn't actually return anything
- Big thanks to [belfazt](https://github.com/belfazt) for the pull request!

## [5.0.1] - 2017-08-29
### Fixed
- Pull #337, fixes issue #366
- On install, some experienced: `ValueError: ("Expected ',' or end-of-list in", 'python-http-client ==3.0.*', 'at', '*')`

## [5.0.0] - 2017-08-11
### BREAKING CHANGE
- The breaking change actually happened in [version 4.2.1](https://github.com/sendgrid/sendgrid-python/releases/tag/v4.2.1), where I mistakenly applied a patch version bump. See issues #328 and #321 for details.
- This version (5.0.0) replaces error handling via HTTPError from urllib in favor of custom error handling via the [HTTPError class](https://github.com/sendgrid/python-http-client/blob/master/python_http_client/exceptions.py) as was the case in version 4.2.0.

## [4.2.1] - 2017-08-03 ##
### Fixed
- Issue #321: Installing 4.2.0 installs the wrong version of python-http-client
- Big thanks to [w-](https://github.com/w-) for the heads up!

## [4.2.0] - 2017-06-01 ##
### Added
- Pull #318 Add ability to reset request headers on client attribute
- Big thanks to [w-](https://github.com/w-) for the pull request!

## [4.1.0] - 2017-05-08 ##
### Added
- Pull #314 Add ability to impersonate subuser
- Big thanks to [w-](https://github.com/w-) for the pull request!

## [4.0.0] - 2017-04-05 ##
### BREAKING CHANGE
- Pull #244 [refactor helpers using property getter/setter](https://github.com/sendgrid/sendgrid-python/pull/244/files)
- Big thanks to [Denis Vlasov](https://github.com/denis90) for the pull request!
- The changes break the implementation of the [Mail Helper](https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/mail) `Mail()` class
- `set_from()` is now the property `from_email`
- `set_subject()` is now the property `subject`
- `set_template_id()` is now the property `template_id`
- `set_send_at()` is now the property `send_at`
- `set_batch_id()` is now the property `batch_id`
- `set_asm()` is now the property `asm`
- `set_ip_pool_name()` is now the property `ip_pool_name`
- `set_mail_settings()` is now the property `mail_settings`
- `set_tracking_settings()` is now the property `tracking_settings`
- `set_reply_to()` is now the property `reply_to`
- `personalization.set_send_at()` is now the property `personalization.send_at`
- `personalization.set_subject()` is now the property `personalization.subject`
- `attachment.set_content()` is now the property `attachment.content`
- `attachment.set_type()` is now the property `attachment.type`
- `attachment.set_filename()` is now the property `attachment.filename`
- `attachment.set_disposition()` is now the property `attachment.disposition`
- `attachment.set_content_id()` is now the property `attachment.content_id`
- `mail_settings.set_bcc_settings()` is now the property `mail_settings.bcc_settings`
- `mail_settings.set_bypass_list_management()` is now the property `mail_settings.bypass_list_management`
- `mail_settings.set_footer_settings()` is now the property `mail_settings.footer_settings`
- `mail_settings.set_sandbox_mode()` is now the property `mail_settings.sandbox_mode`
- `mail_settings.set_spam_check()` is now the property `mail_settings.spam_check`
- `tracking_settings.set_click_tracking()` is now the property `click_tracking`
- `tracking_settings.set_open_tracking()` is now the property `open_tracking`
- `tracking_settings.set_subscription_tracking()` is now the property `subscription_tracking`
- `tracking_settings.set_ganalytics()` is now the property `ganalytics`

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
- Suppression Unsubscribes [GET]

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
- Web API v3 endpoints: apikeys, ASM groups and ASM suppressions

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
