# Changelog

## [Unreleased]

## [1.1.0] - 2026-11-06

### Added
- Case-insensitive exact category search with padded/blank input handling.
- Optional reverse=True in cart sorting methods and copy-returning sort helpers.

### Fixed
- Includes the Unicode-equivalence search repair from the 1.0.1 maintenance line.

## [1.0.1] - 2026-11-06

### Fixed
- Canonically equivalent Unicode title searches now match through NFC normalization.

## [1.0.0] - 2026-11-06

### Added
- Lab 02 cart details, normalized title search and use-case documentation.
- Lab 03 unittest regression suite, real conflict resolution and merge-revert evidence.
- Baseline/release management with annotated tags and reproducible archives.

### Fixed
- Fractional discounts now use Decimal arithmetic and validate finite percentages.

### Baseline notes
- The supplied initial code already had the 20-DVD limit, case-insensitive search,
  discount and ascending sort helpers. Lab 03 labels its seeded limit exercise
  explicitly; these pre-existing features are not claimed as new release changes.
