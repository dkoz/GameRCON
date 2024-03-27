# GameRCON Client
This is a console based RCON for most games that utilize source rcon.

## Supported Games
- Minecraft
- Ark: Survival Ascended
- Palworld
- Path of Titans
Any game using the [Source RCON Protocol](https://developer.valvesoftware.com/wiki/Source_RCON_Protocol)

## Usage
> gamercon -host "127.0.0.1" -port "25575" -pass "rcon passoord" -command "Info"

Options
- -host
  - Server address (default: 127.0.0.1)
- -port
  - RCON Port (default: 25575)
- -pass
  - RCON/Admin Password
- -command
  - Execute a command
