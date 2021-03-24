# LaunchBar-Actions

## Installation
To install these LaunchBar (LB) actions please follow these steps:

1. Clone this repo
2. Copy the LB actions into `~/Library/Application Support/LaunchBar/Actions/`
3. Profit.

## Actions
### battime
battime returns the time left for charging or discharging your Mac.

### bt\_restart
bt\_restart will restart your Macs Bluetooth adapter. It requires the following:

- **[bt\_restart](https://github.com/bryanheinz/bin/blob/master/bt_restart)** installed into `~/Documents/dev/bin/bt_restart` (or the action's script path fixed to your location)
- **[blueutil](https://github.com/toy/blueutil)** installed into `/usr/local/bin/blueutil` (or bt\_restart updated to point at the correct blueutil path)

This will turn off your Bluetooth adapter, wait 1 seconds, and then turn it back on. The LB window should close when it's finished.

### Copy Safari URLs
Copy Safari URLs will copy all of the open tab URLs in the front most Safari window to your clipboard.

### macaddr
macaddr converts the following MAC address strings:

- 00:00:00:00:00:00 → 000000000000
- 000000000000 → 00:00:00:00:00:00
- 00-00-00-00-00-00 → 00:00:00:00:00:00

Results will be copied to the clipboard.

### man
Opens the manual page for the given command in Preview.app.

### Songwhip
[Songwhip](https://songwhip.com) takes a music streaming service URL and creates a Songwhip page for it, and then copies that URL to the clipboard.

Requires:
- Python 3
- Python Requests module

### uuidgen
uuidgen generates a UUID and copies it to your clipboard.
