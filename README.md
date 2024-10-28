# GameRCON Client v0.1.3
 This is a console based RCON Client for games that utilize an RCON protocol

## Supported Games
- Minecraft
- Garry's Mod
- Rust
- Ark: Survival Ascended
- Ark: Survival Evolved
- Palworld
- Path of Titans

 Runs any game using the [Source RCON Protocol](https://developer.valvesoftware.com/wiki/Source_RCON_Protocol).

## Compile
> You can compile from source using the `build.bat` or `build.sh`

## Usage
> Regular RCON
```
gamercon --host "127.0.0.1" --port "25575" --pass "rcon passoord" --command "Info"
```

> Base64 RCON
```
gamercon-b64 --host "127.0.0.1" --port "25575" --pass "rcon passoord" --command "Info"
```

> Options output
```
options:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  Server host address
  -P PORT, --port PORT  Server RCON port
  -p PASSWORD, --password PASSWORD
                        Server RCON password
  -c COMMAND, --command COMMAND
                        Command to execute on the server
  -v, --version         show program's version number and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Connection timeout in seconds (optional)
```

## Batch Script
> Example batch script for quick rcon execution. Example: `./file.bat Command`
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

.\gamercon -H %HOST% -P %PORT% -p %PASS% -c "%COMMAND%"
```