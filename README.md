# MYCLI

```
 chat   --user "Konstantin"   --log   send   "My message"   --to "Alexander"   --insert-signature
└┬───┘ └┬──────────────────┘ └┬────┘ └┬───┘ └┬───────────┘ └┬───────────────┘ └┬─────────────────┘
 │      │                     │       │      │              │                  └── subcommand's flag
 │      │                     │       │      │              └── subcommand's named argument with value
 │      │                     │       │      └── subcommand's positional argument
 │      │                     │       └── subcommand name
 │      │                     └── command's flag
 │      └── command's named argument with value
 └── command name
```

## Tests
```bash
uvx tox
uvx tox run -e 3.11 -- "<path_to_test>"
```
