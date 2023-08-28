# `spin-numpy-example`

This is an example of how to use [componentize-py] and [NumPy] to build a [Spin]
application.

[componentize-py]: https://github.com/dicej/componentize-py
[NumPy]: https://numpy.org
[Spin]: https://github.com/fermyon/spin

## Prerequisites

* `componentize-py` 0.4.0
* `NumPy`, built for WASI
* `Spin` branch `wasmtime-592ddc52`
* `Rust` (specifically, `Cargo`) for installing `Spin`

Note that we use an unofficial build of NumPy since the upstream project does
not yet publish WASI builds.  Also, we use a branch of Spin which depends on a
compatible build of Wasmtime.

```
cargo install --locked --git https://github.com/fermyon/spin --branch wasmtime-592ddc52
pip install componentize-py
curl -OL https://github.com/dicej/wasi-wheels/releases/download/canary/numpy-wasi.tar.gz
tar xf numpy-wasi.tar.gz
```

## Building and running

First, build the app and run it:

```
spin build --up
```

Then, in another terminal, use cURL to send a request to the app:

```
curl -i -H 'content-type: application/json' \
    -d '[[[1, 2], [4, 5], [6, 7]], [[1, 2, 3], [4, 5, 6]]]' \
    http://127.0.0.1:3000/multiply
```

The above should return the response body `[[9, 12, 15], [24, 33, 42], [34, 47, 60]]`.
