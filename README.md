<p align="center">
    <img src="https://bit.ly/39k5XBT" alt="twhook">
</p>
<p align="center">
    <img src="https://bit.ly/3jWHiJZ" alt="py">
    <img src="https://bit.ly/2Xvcash" alt="twt-api">
    <img src="https://bit.ly/38WBrOt" alt="mit">
</p>

## About
twhook is a simple Twitter Premium Account Activity API wrapper that helps you to manage webhooks and subscriptions.

## Installation
Git:
```bash
git clone https://github.com/nxgeo/twhook.git
cd twhook
pip install -r requirements.txt
```
Pip:
```bash
pip install twhook
```

## Examples
For easy implementation examples, see [twhook/examples/](https://bit.ly/3CseaAr).

## Suggestion
As described in the [Twitter Securing Webhooks](https://bit.ly/3AnGjZ2) guide, a first step is writing code that receives a Twitter Challenge-Response Check (CRC) GET request and responds with a properly formatted JSON response.

A CRC will be sent when you register your webhook URL, so implementing your CRC response code is a fundamental first step.

[HERE](https://bit.ly/3ClNq4P) is an example of implementing a CRC response in Python.

## Reference
[Account Activity API: Premium](https://bit.ly/3zg8JTq)