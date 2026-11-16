# KinCheck

A paper protocol for checking who is really on the phone.

Two people each hold the same printed table of one-time word lines, one table per pair of people. To check a caller, one person reads a line number and its ask word, the other replies with that line's two answer words, and both cross the line out. A cloned voice can't pass, because the check is about what you hold, not how you sound.

- **Protocol spec (v1.0 draft):** https://klabianco.github.io/kincheck/
- **Make and print cards:** https://klabianco.github.io/kincheck/cards.html

The card maker is a single HTML file. It makes no network requests (enforced by Content-Security-Policy) and stores nothing, so you can also save it and use it offline.

## Building

`index.html` and `cards.html` are generated from `src/`:

```sh
python3 build.py
```

The build rejects the word list unless it has exactly 256 unique words of at most 9 letters, with no rhyming endings except pairs reviewed by ear.

## Limits

The protocol does not stop a live relay between two real people, a lost or photographed card, or coercion. See §4 of the spec.

## License

MIT, covering the spec, the word list and the code. Build on it.
