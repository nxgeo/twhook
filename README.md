<p align="center">
    <img src="https://bit.ly/39k5XBT" alt="twhook">
</p>

## About
Twhook is a simple Twitter Premium Account Activity API wrapper that helps you to manage webhooks and subscriptions.

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
For basic implementation, see [twhook/examples](https://github.com/nxgeo/twhook/tree/master/examples).

## Suggestion
As described in the [Twitter Securing Webhook](https://developer.twitter.com/en/docs/twitter-api/premium/account-activity-api/guides/securing-webhooks) guide, the first step is writing code that receives a Twitter Challenge-Response Check (CRC) GET request and responds with a properly formatted JSON response.

A CRC will be sent when you register your webhook URL, so implementing your CRC response code is a fundamental first step.

[Here](https://gist.github.com/nxgeo/74f35a3ab5951740892f811a83f2d403) is an example of implementing a CRC response in Python.

## Reference
[Account Activity API: Premium](https://developer.twitter.com/en/docs/twitter-api/premium/account-activity-api)