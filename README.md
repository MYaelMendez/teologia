# 🏵️ TEOLOGIA · διδαχή

**One Gospel · Many Languages · Every Generation.**

An open, versioned, multilingual learning infrastructure for the Latin American Lutheran Institute (LALI).

**διδαχή** is the teaching. **ἐγχειρίδιον** is its portable handbook. **9:16** is our contemporary handheld interface.

> Faith passed from hand to hand. Knowledge passed from repo to repo.

## Start here

- [Español](README.es.md) · [English](README.md) · [Português](README.pt-BR.md)
- [Biblioteca Luterana · Multilingual reference library](biblioteca/README.md)
- [The Enchiridion](content/enchiridion/README.md)
- [Curriculum and translation contract](docs/CONTENT-CONTRACT.md)
- [Contribution guide](CONTRIBUTING.md)
- [Learning interface](apps/handbook/index.html)

## Principles

1. **Scripture and confessional fidelity:** cite primary sources and editions; distinguish canonical text from commentary.
2. **Open education:** every lesson has a stable ID, learning outcomes, sources, a human reviewer, and a reusable activity.
3. **Multilingual by design:** English, Spanish and Brazilian Portuguese are first-class; original-language texts are referenced with provenance.
4. **Mobile-first:** the 9:16 handbook works without accounts, telemetry, or an AI provider.
5. **Forkable:** learners can copy the curriculum, create artifacts and teach others.
6. **Human authority:** AI may assist research and translation but does not approve doctrine or inherit human authority.

## Repository map

```text
apps/handbook/         static 9:16 learning interface
biblioteca/            curated multilingual library catalog
content/enchiridion/   catechism learning modules (not unattributed editions)
content/lessons/       language-independent lesson metadata
i18n/                  localized interface and lesson content
docs/                  editorial and provenance standards
scripts/               content validation
.github/workflows/     CI checks
```

## Status

**v0.1 foundation.** Initial examples are editorial scaffolding, not an official translation of Luther's Small Catechism. Publication, licensing and doctrinal review must be confirmed before importing third-party texts. Existing materials on myaelmendez.github.io are candidates for a reviewed inventory, not automatically copied.

## Development

Open `apps/handbook/index.html` in a browser for the zero-build preview. Run `python3 scripts/validate.py` to check locale parity and lesson metadata.

**Teologia.ai** is the intended public doorway; domain routing and GitHub Pages deployment are not yet configured.
