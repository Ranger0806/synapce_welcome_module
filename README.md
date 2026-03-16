# Synapse Welcome Module

A simple module for Matrix Synapse that sends a welcome message to newly registered users via the Synapse Admin API.

## Features

* Listens for new user registrations using `register_account_validity_callbacks`
* Automatically sends a welcome message to the user
* Supports HTML-formatted messages
* Uses the Synapse **Server Notice** system

## How it works

1. The module registers the `on_user_registration` callback.
2. When a new user registers, Synapse triggers the callback.
3. The module sends a request to:

```
/_synapse/admin/v1/send_server_notice
```

4. The user receives a welcome message from the server.

## Configuration

Add the module to your `homeserver.yaml`:

```yaml
modules:
  - module: welcome_module.WelcomeModule
    config:
      token: "ADMIN_ACCESS_TOKEN"
      path: "/data/welcome.html"
```

### Parameters

| Parameter | Description                      |
| --------- | -------------------------------- |
| `token`   | Synapse admin access token       |
| `path`    | Path to the HTML welcome message |

## Example welcome.html

```html
<h2>Welcome!</h2>
<p>You have successfully registered on this Matrix server.</p>
```

## Requirements

* Python 3.10+
* Synapse 1.39+

## Installation

Place the module file in your Synapse environment and restart the server.

```bash
systemctl restart matrix-synapse
```

## License

MIT
