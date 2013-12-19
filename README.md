# sentry-nameko

This library provides an custom Data Interface for Sentry allowing you to better
integrate [Nameko](https://github.com/onefinestay/nameko) Call ID Stacks in your
logged events.

## Installing and Prerequisites

You need Sentry installed. Instructions can be found
[here](http://sentry.readthedocs.org/en/latest/quickstart/index.html).

Install sentry-nameko into the virtualenv that your Sentry instance is installed
in:

```bash
pip install sentry-nameko
```

In your sentry config (by default, at `~/.sentry/sentry.conf.py`), you need to
extend the `SENTRY_ALLOWED_INTERFACES` setting to include our custom interface.
You'll probably want something like this:

```python
SENTRY_ALLOWED_INTERFACES = SENTRY_ALLOWED_INTERFACES.union(
    ['sentry_nameko.CallIdStack',]
)
```

## Logging events example

Presuming you're using built-in `logging`, and you've set up handlers to hit
sentry, you can provide Call ID data to Sentry like so:

```python

# worker_ctx is a WorkerContext instance

logger.log(
    log_level,
    message,
    extra={
        'tags': {
            'call_id': worker_ctx.call_id,
            'parent_call_id': worker_ctx.immediate_parent_call_id,
        },
        'sentry_nameko.CallIdStack': {
            'call_id_stack': worker_ctx.call_id_stack,
        },
    },
)

```

The tagging of the `call_id` and `parent_call_id` fields enables searches to be
performed on events accordingly. The use of `sentry_call_id_stack.CallIdStack`
triggers the custom data interface.

## Contributing

`sentry-nameko` is developed on GitHub, primarily by the development team at
[onefinestay](http://www.onefinestay.com). The GitHub repository is
https://github.com/onefinestay/sentry-nameko.

You are welcome and encouraged to contribute comments, suggestions, patches
and feature requests.

## License

Apache 2.0. See LICENSE for details.
