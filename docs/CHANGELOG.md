## 1.11.0 [August 2024]

### Added

- This file, `CHANGELOG.md`.
- Launch docs website.
- Duplicate request (with new request popup) under cursor in tree with ++d++.
- "Quick" duplicate request (without new request popup, request name is auto-generated) under cursor in tree with ++shift+d++.
- Delete request (with confirmation modal) under cursor in tree with ++backspace++.
- "Quick" delete request (without confirmation modal) under cursor in tree with ++shift+backspace++.
- "Quit Posting" added to command palette.
- Move the sidebar to the right or left using `collection_browser.position: 'right' | 'left'` config.
- Refinements to "galaxy" theme.
- "galaxy" theme is now default.
- Help text added to "empty state" in the collection browser.
- Extend info in the "Collection Browser" help modal.
- Visual indicator (a red bar on the left) on Input fields that contain invalid values.
- Toast message now appears when trying to submit the 'new request' modal with invalid values.
- Public roadmap (initial brain-dump version).

### Fixed
- Ensure the location of the request on disk in the `Info` tab wraps instead of clipping out of view.
- Inserting requests in sorted position on creation.
- Prevent creating requests with no name.
- Prevent writing paths in the file-name field in the new request modal.
- Prevent specifying paths outside of the open collection dir in the directory field in the new request modal.
- Fix variables not being substituted into several fields, including auth.

### Changed

- Upgrade to Textual version 0.76.0
- Change logic to render bindings in help modal to reflect new Textual API.
- Sort order of requests in the tree improved.


---

!!! note
    Changes prior to 1.11.0 are not documented here.
    Please see the [Releases page](https://github.com/darrenburns/posting/releases) on GitHub for information on changes prior to 1.11.0.