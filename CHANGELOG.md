# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Changed
- Web interface external links open in new browser tab.
- Web interface lists are sorted alphabetically.
- Web interface nav items relect active state on click.
- Web interface jumps to correct location on selection of list.
- Updates to resolve pylint messages in myplex.py.

### Added
- Added simple tests to myplex.py.
- Travis-CI automated testing on push.

## [v0.8.0] - 2017-02-19
### Added
- .editorconfig to ensure coding styles are kept the same. [editorconfig](http://editorconfig.org/)
- This CHANGELOG file.
- Ability to sync ahead only X files.
- Ability to remove watched items that are already synced.
- Default user.ini.config file, to be renamed to user.ini for new instances.

### Changed
- Changed logging format to a nicer layout.
- Paths in default user.ini changed to Windows paths.
- Update plexdl.py, webui.py to conform to python coding standards.
- Version numbers displayed now come from a shared version file (version.py).

### Fixed
- Fix Plex server path in README.
- Removed leftover bootstrap docs js file in web template.

### Removed
- Remove user.ini file from repo.

## [v0.7.0] - 2015-07-20

## [v0.6.0] - 2015-07-15

## [v0.5.0] - 2015-07-11

## [v0.4.0] - 2015-03-28

## [v0.3.0] - 2014-08-12

## [v0.2.0] - 2014-07-30

## v0.1.0 - 2014-07-28

[Unreleased]: https://github.com/danstis/PlexDownloader/compare/v0.8.0...HEAD
[v0.8.0]: https://github.com/danstis/PlexDownloader/compare/v0.7.0...v0.8.0
[v0.7.0]: https://github.com/danstis/PlexDownloader/compare/v0.6.0...v0.7.0
[v0.6.0]: https://github.com/danstis/PlexDownloader/compare/v0.5.0...v0.6.0
[v0.5.0]: https://github.com/danstis/PlexDownloader/compare/v0.4.0...v0.5.0
[v0.4.0]: https://github.com/danstis/PlexDownloader/compare/v0.3.0...v0.4.0
[v0.3.0]: https://github.com/danstis/PlexDownloader/compare/v0.2.0...v0.3.0
[v0.2.0]: https://github.com/danstis/PlexDownloader/compare/v0.1.0...v0.2.0
