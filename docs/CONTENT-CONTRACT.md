# Content contract v0.1

Every lesson must include: `id`, `title`, `source`, `source_edition`, `license`, `review_status`, `reviewer`, `updated`, `languages`, `outcomes`, and `activity`.

Locale keys: `en`, `es`, `pt-BR`. Language-independent identifiers must not change in translation. `review_status` may be `draft`, `in-review`, or `approved`; AI-generated material always starts as `draft`. Do not label an official catechism translation without verifying edition and rights. Original-language excerpts require manuscript/edition citation.

Use human-readable Markdown and JSON. No runtime agent may automatically approve or publish doctrinal content.
