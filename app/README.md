# UI - Info

## Pre-requirements

- [Node.js](https://nodejs.org/en/)

## Setup App

The following command install expo-cli in your system globaly.

```bash
npm install -g expo-cli
```

## App visualization

Run the following command inside the app folder:

```bash
npm start
```

## Errors and Fixes

- Incorrect node version: `Your project is in SDK version >= 33.0.0, but the expo package version seems to be older`Use LTS version of node 12.16.1

- Unsecure connection: `Could not load exp:[IP] Network response time out.` => use `expo start --tunnel`
