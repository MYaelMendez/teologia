# Biblioteca Luterana · catalog contract

The `catalog.json` file has `schema_version` and `records`. Each record requires a stable `id`, `type`, `collection`, `titles` with `en`, `es`, `pt-BR`, `creator`, `original_year`, `original_language`, `edition`, `source_url`, `rights`, `review_status`, and `digital_copy_available`.

`review_status`: `draft`, `in-review`, `approved`. `source_url: null` means no verified external edition is selected. A bibliographic work record must never be mistaken for a hosted full-text edition. When adding a full-text edition, separately document translator, publisher, publication year, license, canonical URL, citation format, accessibility, and human reviewer. Rights to an original historical work do not imply that modern translations or critical editions are public domain.
