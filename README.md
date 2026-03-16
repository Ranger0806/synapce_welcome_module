# Synapse Welcome Module

A lightweight module for Matrix Synapse that sends a welcome message to newly registered users using the Synapse Admin API.

The module reads a message from a file and sends it to the user after registration.

---

## Features

* Sends a welcome message automatically after user registration
* Reads message content from an external file
* Supports plain text and HTML-formatted messages
* Uses Tornado `AsyncHTTPClient` to communicate with the Synapse Admin API

---

## How it works

1. The module registers the `on_user_registration` callback.
2. When a new user registers, Synapse triggers the callback.
3. The module sends an HTTP request to the Synapse Admin API endpoint:

```
/_synapse/admin/v1/send_server_notice
```

4. The user receives the welcome message from the server.

---

## Configuration

Add the module to your `homeserver.yaml` configuration:

```yaml
modules:
  - module: welcome_module.WelcomeModule
    config:
      token: "ADMIN_ACCESS_TOKEN"
      path: "/data/welcome.html"
```

### Parameters

| Parameter | Description                                           |
| --------- | ----------------------------------------------------- |
| `token`   | Synapse admin access token used to call the Admin API |
| `path`    | Path to the file containing the welcome message       |

---

## Example message file

Example `welcome.html`:

```html
<h2>Welcome!</h2>
<p>You have successfully registered on this Matrix server.</p>
```

The file content will be used both as the message body and the formatted HTML body.

---

## Requirements

* Python 3.10+
* Synapse 1.39+
* Tornado

---

## Installation

1. Place the module file somewhere accessible by Synapse.

Example:

```
/etc/matrix-synapse/modules/welcome_module.py
```

2. Add the module configuration to `homeserver.yaml`.

3. Restart Synapse:

```bash
systemctl restart matrix-synapse
```

---

## License

MIT
