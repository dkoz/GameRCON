# GameRCON Client
This is a console based RCON Client for games that utilize source rcon.

## Supported Games
- Minecraft
- Ark: Survival Ascended
- Palworld
- Path of Titans

Runs any game using the [Source RCON Protocol](https://developer.valvesoftware.com/wiki/Source_RCON_Protocol).

## Usage
> gamercon -host "127.0.0.1" -port "25575" -pass "rcon passoord" -command "Info"

**Options**
- -host "127.0.0.1"
  - Server address (default: 127.0.0.1)
- -port "25575"
  - RCON Port (default: 25575)
- -pass "rcon password"
  - RCON/Admin Password
- -command "Info"
  - Execute a command

## Batch Script

```
@echo off
set HOST=host here
set PORT=rcon port here
set PASS=rcon pass here

set COMMAND=%1
shift
:Loop
if "%1"=="" goto Continue
set COMMAND=%COMMAND% %1
shift
goto Loop
:Continue

.\gamercon -host %HOST% -port %PORT% -pass %PASS% -command "%COMMAND%"
```